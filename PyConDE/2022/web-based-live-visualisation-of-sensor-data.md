Web based live visualisation of sensor data
===========================================
Data being read out from a sensor should be presented on multiple end devices via web interface.
The hardware is a Raspberry Pi equipped with an orientation sensor.
Sensor data will be published to a Redis channel.
FastAPI is used to provide the web interface including a websocket for continuous data update.
The data is visualised as time series using plotly.js as well as a moving 3D model using three.js.
Limitations of the setup regarding sample rate, response time as well as number of consumers will be discussed.
A mobile WLAN access point will be provided to enable the audience to interact with the presented setup.

Author
------
**Dr. Jannis Lübbe** ([GitHub](https://github.com/jaluebbe), [Twitter](https://twitter.com/jannis_luebbe))

[![Web based live visualisation of sensor data](https://img.youtube.com/vi/o_cr-RmGmio/0.jpg)](https://www.youtube.com/watch?v=o_cr-RmGmio)
