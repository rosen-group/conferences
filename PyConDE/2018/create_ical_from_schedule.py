"""Generate an iCal file from the PyCon.DE 2018 online schedule

The calendar written is not complete. This is especially the case for events
spanning multiple rows (aka time slots).
"""

from collections import defaultdict
import datetime
import difflib
import uuid

from bs4 import BeautifulSoup, Comment
import icalendar as ical
import pytz
import requests

DATES = {'wed': (24, 10, 2018),
         'thu': (25, 10, 2018),
         'fri': (26, 10, 2018),
         'sat': (27, 10, 2018),
         'sun': (28, 10, 2018),
         }

TZ_EUROPE_BERLIN = pytz.timezone('Europe/Berlin')


def create_event(action, date, location, time_axis):
    """Create and ical event based on input parameters.

    Parameters
    ----------
    action : dict
    date : datetime.datetime
    location : str
    time_axis : list(int)

    Returns
    -------
    event : `icalendar.Event`
    """
    event = ical.Event()

    event['UID'] = uuid.uuid4()

    now = datetime.datetime.now(tz=TZ_EUROPE_BERLIN)
    event['DTSTAMP'] = ical.vDatetime(now).to_ical()

    event['DTSTART'] = ical.vDatetime(date).to_ical()
    try:
        start = difflib.get_close_matches('{:02d}:{:02d}'
                                          .format(date.hour,
                                                  date.minute),
                                          time_axis,
                                          n=1)[0]
        start_index = time_axis.index(start)

        end_index = min(start_index + 1, len(time_axis) - 1)

        hour, minute = map(int, time_axis[end_index].split(':'))

        end = datetime.datetime(date.year,
                                date.month,
                                date.day,
                                hour,
                                minute,
                                tzinfo=TZ_EUROPE_BERLIN)
    except ValueError as ve:
        end = date + datetime.timedelta(minutes=30)
    event['DTEND'] = ical.vDatetime(end).to_ical()
    event['LOCATION'] = location
    event['SUMMARY'] = action['title']
    if 'presenter' in action:
        event['ORGANIZER'] = action['presenter']
    # event[''] = action['tags']
    return event


def create_calendar(actions, location_and_time_axes):
    """Create a calendar in ical format

    Parameters
    ----------
    actions : dict
    location_and_time_axes : dict

    Returns
    -------
    calendar : `icalendar.Calendar`
    """
    calendar = ical.Calendar()
    calendar['PRODID'] = '{} {}'.format(ical.__name__, ical.__version__)
    calendar['VERSION'] = 2.0
    calendar['X-WR-CALNAME'] = 'PyCon.DE 2018'

    for location, date in actions.keys():
        meta_info = location_and_time_axes[(date.year, date.month, date.day)]
        time_axis = meta_info['time_axis']
        for action in actions[(location, date)]:
            if action['title'] == 'End':
                continue

            event = create_event(action, date, location, time_axis)

            calendar.add_component(event)

    return calendar


def query_page():
    session = requests.Session()
    return session.get('https://de.pycon.org/schedule/', verify=False)


def parse_page(page):
    """Parse website

    Parameters
    ----------
    page : `requests.Response`

    Returns
    -------
    (actions, location_and_time_axes) : tuple(dict, dict)
    """
    soup = BeautifulSoup(page.content, 'lxml')

    actions = defaultdict(list)
    location_and_time_axes = defaultdict(lambda : defaultdict(list))

    for table in list(soup.find_all('table')):

        heading = table.find_previous_sibling('h2')
        _, date_string = heading.string.strip().split(' ')
        date = datetime.datetime.strptime(date_string, '%d.%m.%Y')
        date = date.replace(tzinfo=TZ_EUROPE_BERLIN)

        thead = table.find('thead')

        locations = []
        for table_header in list(thead.find_all('th'))[1:]:
            locations.append(table_header.string)

        body = table.find('tbody')

        time_axis = []
        year = date.year
        month = date.month
        day = date.day

        for row in body.find_all('tr'):
            cells = row.find_all('td')

            if 'id' in row.attrs and row['id']:
                time = row['id'].strip().split('-')[1]
            else:
                time = cells[0].string.strip()

            time_axis.append(time)

            for idx, cell in enumerate(cells[1:]):
                content = cell.string
                if content is None:
                    talk = cell.find('b')
                    presenter = cell.find('i')
                    tags = cell.find('span', 'tags')
                    if talk and talk.string is not None:
                        if tags and tags.string:
                            tags = tags.string.strip().encode('ascii',
                                                              'replace')
                        else:
                            tags = ''

                        day, time = row['id'].split('-')
                        (day, month, year) = DATES[day]
                        hour, minute = map(int, time.split(':'))
                        date = datetime.datetime(year,
                                                 month,
                                                 day,
                                                 hour,
                                                 minute,
                                                 tzinfo=TZ_EUROPE_BERLIN)

                        title = talk.string.strip().encode('ascii', 'replace')

                        presenter = presenter.string.strip().encode('ascii',
                                                                    'replace')

                        location = locations[idx]

                        actions[(location, date)].append({'title': title,
                                                          'presenter': presenter,
                                                          'tags': tags})
                    elif len(list(cell.descendants)) > 0:
                        title = cell.find('a').string
                        hour, minute = map(int, time.split(':'))
                        date = date.replace(hour=hour, minute=minute)
                        actions[('', date)].append({'title': title})
                elif not isinstance(content, Comment):
                    hour, minute = map(int, time.split(':'))
                    date = date.replace(hour=hour, minute=minute)
                    actions[('', date)].append({'title': cell.string.strip()})

        if year and month and day:
            time_axis = sorted(time_axis)
            location_and_time_axes[(year,
                                    month,
                                    day)]['time_axis'] += time_axis
            location_and_time_axes[(year,
                                    month,
                                    day)]['locations'] += locations

    return actions, location_and_time_axes


if __name__ == '__main__':
    page = query_page()

    actions, location_and_time_axes = parse_page(page)

    calendar = create_calendar(actions, location_and_time_axes)

    now = datetime.datetime.now(tz=TZ_EUROPE_BERLIN)

    with open('PyConDE2018_{}.ics'.format(now.strftime('%Y%m%d%H%M')),
              'wb') as ics_file:
        ics_file.write(calendar.to_ical())
