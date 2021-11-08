import datetime
import os
from influxdb import client as influxdb


#InfluxDB Connection Details
influxHost = 'localhost'
influxUser = 'admin'
influxPasswd = 'pass'

#InfluxDB data
influxdbName = 'database_name'

#return influxDB friendly time 2017-02-26T13:33:49.00279827Z (not really required, but meh)
current_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

temperature = 25.3
humidity = 98

influx_metric = [{
    'measurement': 'SensorsData',
    'time': current_time,
    'fields': {
        'temperature': temperature,
        'humidity': humidity
    }
}]

#Saving data to InfluxDB
try:
    db = influxdb.InfluxDBClient(influxHost, 8086, influxUser, influxPasswd, influxdbName)
    db.write_points(influx_metric)
finally:
    db.close()