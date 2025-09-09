import os	#to access environmental variable
import time	#to get timestamp
import random	#to generate random sensor value

sensor_type = os.getenv("SENSOR_TYPE")
if not sensor_type:
	raise ValueError("Environment variable SENSOR_TYPE is not set. Use: export SENSOR_TYPE=temperature")

value = round(random.uniform(1.0, 40.0), 2)
timestamp = time.strftime("[%Y-%m-%d] [%H:%M:%S]")
print("{} - {}: {}".format(timestamp, sensor_type, value))

