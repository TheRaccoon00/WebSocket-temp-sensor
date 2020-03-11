# WebSocket-temp-sensor

Websocket application which get informations from temperature sensor

## Getting Started

What you need to install before:

* Python3
* Mariadb server

### Prerequisites

I've done a script to install python libraries and to configure maradb server (create database and user).

```
chmod +x configure.sh
./configure.sh
```

### Run application

First of all, you need to run the web application.

```
python3 app.py
```

Now, you need to got a the following address: http://localhost:5000/

It will be normally a single web page with an empty table.

## Run the simulator

Now, we want to see informations coming by themselves. So you have to run the simulation of the sensor in the folder Sensor_simulation.

```
python3 simul_sensor.py
```

And then, let's go back to the web application see the result. (1 line for each 3 seconds)
