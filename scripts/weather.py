# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# -- Libraries  ----------------------------------------------------------------
import pywapi
import pprint
import time

# -- Confiurations  ------------------------------------------------------------
# the city name you want to search
CITY_NAME = 'York, YOR, United Kingdom'

# this defines the update time (s) of the weather data
UPDATE_TIME = 30

# -- Main Program  -------------------------------------------------------------
# (no need to change contents below this line)

# find the city_id from weather.com
city_list = pywapi.get_loc_id_from_weather_com(CITY_NAME)


cnt = city_list['count']
print 'Warning: we found ' + str(cnt) + ' possible cities, ' + \
    		'We will use the first one!'
for i in range(cnt):
    print city_list[i]
city_id = city_list[0][0]

# main loop
while True:
	try:
		# retrive weather data from weather.com
		weather_info = pywapi.get_weather_from_weather_com(city_id)

		# print raw data (debug only)
		print '\nRaw Retrived Data:'
		pp = pprint.PrettyPrinter(indent=4)
		pp.pprint(weather_info)

		# get units
		units = {}
		units['distance'] = weather_info['units']['distance']
		units['pressure'] = weather_info['units']['pressure'] 
		units['rainfall'] = weather_info['units']['rainfall']
		units['speed'] = weather_info['units']['speed']
		units['temperature'] = weather_info['units']['temperature']

		# output current condition
		print '[City]'
		print weather_info['location']['name']
		print '\n[Current]'
		print 'Description: ' + weather_info['current_conditions']['text']
		print 'Temperature: ' + weather_info['current_conditions']['temperature'] + \
				' ' + units['temperature']
		print 'Humidity: ' + weather_info['current_conditions']['humidity'] +'%'
		print weather_info['current_conditions']['wind']

		# forecasts
		print '\n[Forecast]'
		for i in weather_info['forecasts']:
			print i['date'] + ',' + i['day_of_week'] + ': ' \
					+ i['day']['brief_text'] + ', ' \
					+ i['low'] + '-' + i['high'] + ' ' + units['temperature']

		# package data into a string
		weather_str = weather_info['location']['name'] + ';' \
					  + weather_info['current_conditions']['text'] + ';' \
					  + weather_info['current_conditions']['temperature'] + ';' \
					  + weather_info['current_conditions']['humidity'] + ';' \
					  + weather_info['forecasts'][0]['high'] + ';' \
					  + weather_info['forecasts'][0]['low'] + ';\n'

	
	except URLError:
		pass
	
	except:
		pass
	
	# sleep
	time.sleep(UPDATE_TIME)
