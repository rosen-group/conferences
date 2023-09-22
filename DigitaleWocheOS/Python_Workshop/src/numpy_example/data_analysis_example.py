'''
Example that loads temperature data from Osnabruecks public data api.
Visualisations are created to showcase functionality of numpy and matplotlib.
'''
import numpy as np  # for working on numerical data
import matplotlib.pyplot as plt  # for visualisations
import requests  # for HTTP requests
import datetime  # to handle timestamps

import warnings # to disable warnings due to SSL certificate missing (can be ignored)

warnings.filterwarnings('ignore')

# Query temperature sensors at HS Osnabrueck, 52.28247, 8.0248, buried underground at 30cm and 60cm depth
# Using requests module to create HTTP requests easily
http_response = requests.get(
    "https://daten-api.osnabrueck.de/v1.1/Things?$filter=substringof('Boden',name)"
    "&$expand=Datastreams($select=name;$filter=substringof('temp',name);$expand="
    "Observations($orderby=resultTime desc;$top=120))",
    verify=False,
)


# Read out sensor data from http response
sensor_times = []
sensor_30cm = []
sensor_60cm = []

all_data = http_response.json()

# create loop over all observations (= measurements of the sensors) and store in a list
for measurement_at_30cm in all_data["value"][1]["Datastreams"][0]["Observations"]:
    sensor_30cm.append(measurement_at_30cm["result"])
    sensor_times.append(
        datetime.datetime.strptime(
            measurement_at_30cm["resultTime"][0:16], "%Y-%m-%dT%H:%M"
        )
    )

for measurement_at_60cm in all_data["value"][1]["Datastreams"][1]["Observations"]:
    sensor_60cm.append(measurement_at_60cm["result"])


# Basic analysis of data using numpy
length_30 = len(sensor_30cm)
length_60 = len(sensor_60cm)
print(f"Datapoints of sensor at 30cm: {length_30} values.")
print(f"Datapoints of sensor at 60cm: {length_60} values. \n")

mean_30 = np.mean(sensor_30cm)
mean_60 = np.mean(sensor_60cm)
print(f"Mean of sensor at 30cm: {mean_30:.2f} °C.")
print(f"Mean of sensor at 60cm: {mean_60:.2f} °C. \n")

var_30 = np.var(sensor_30cm)
var_60 = np.var(sensor_60cm)
print(f"Variance of sensor at 30cm: {var_30:.2f} °C.")
print(f"Variance of sensor at 60cm: {var_60:.2f} °C. \n")


# Plot sensor data over time using matplotlib
plt.figure()
plt.plot(sensor_times, sensor_30cm, "red", label="30cm Tiefe")
plt.plot(sensor_times, sensor_60cm, "blue", label="60cm Tiefe")
plt.legend()
plt.title("Temperatur im Boden, HS Osnabrueck")
plt.xticks(rotation = 45)
plt.ylabel("Temperatur [°C]")
plt.show()

# # Plot variation of data
# plt.figure()
# plt.boxplot(
#     (sensor_30cm, sensor_60cm),
#     patch_artist=True,
#     labels=["30cm", "60cm"],
#     showfliers=False,
# )
# plt.title("Variation der Messwerte")
# plt.ylabel("Temperatur [°C]")
# plt.show()

# # analyse difference based on time of the day
# diff_night = []  # 00 - 06 o'clock
# diff_morning = []  # 06 - 12 o'clock
# diff_day = []  # 12 - 18 o'clock
# diff_evening = []  # 18 - 0 o'clock
# for value30, value60, meas_time in zip(sensor_30cm, sensor_60cm, sensor_times):
#     if meas_time.hour < 6:
#         diff_night.append(value30 - value60)

#     if meas_time.hour < 12:
#         diff_morning.append(value30 - value60)

#     if meas_time.hour < 18:
#         diff_day.append(value30 - value60)

#     else:
#         diff_evening.append(value30 - value60)


# plt.figure()
# labels = ["Nacht", "Morgen", "Tag", "Abend"]
# plt.bar(
#     labels,
#     [
#         np.mean(diff_night),
#         np.mean(diff_morning),
#         np.mean(diff_day),
#         np.mean(diff_evening),
#     ],
# )
# plt.title("30cm Temperatur minus 60cm Temperatur")
# plt.show()
