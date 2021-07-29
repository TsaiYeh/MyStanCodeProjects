"""
File: weather_master.py
Name: 吳采曄 Judy
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant controls when to stop entering new data.
EXIT = -100


def main():
	"""
	This function computes the average temperature, highest temperature, lowest temperature,
	and how many cold days among the input temperature data.
	"""
	print('stanCode \"Weather Master 4.0\"!')
	data = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))		# Let user input temperature data.
	if data == EXIT:												# when user doesn't input temperatures.
		print('No temperatures were entered.')
	else:
		maximum = data												# Maximum is the first input data if no further data input.
		minimum = data												# Minimum is the first input data if no further data input.
		total_data = data  											# Total temperature data is the first data if no further data input.
		day = 1  													# Day is the number of days which contain temperature data. Day is 1 as the first data is input.
		if data < 16:												# Cold_day is the day which temperature is less than 16 degree.
			cold_day = 1											# Cold_day is 1 if the first data is less than 16.
		else:
			cold_day = 0											# Cold_day is 0 day if the first data is equal or larger than 16.
		while True:
			data = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
			day += 1												# Compute the days.
			total_data += data										# New total data equals to old total data plus new data.
			if data == EXIT:										# If user enter EXIT code, break the while loop.
				total_data -= EXIT									# Deduct the EXIT value from total data.
				day -= 1											# Minus one day because EXIT cannot be counted as data.
				break
			if data > maximum:
				maximum = data										# New data will be the maximum because it's larger than original maximum.
			if data < minimum:
				minimum = data										# New data will be the minimum because it's smaller than original maximum.
			if data < 16:											# If the temperature is less than 16 degree.
				cold_day += 1										# Compute the number of cold days.
		average = total_data / day  								# Average is total_data divided by days.
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(average))
		print(str(cold_day) + ' cold day(s)')



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
