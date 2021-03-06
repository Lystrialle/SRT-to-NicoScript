import re

def time_reparser(time):
# Restructures an SRT hh:mm:ss,MMM timecode into NicoScript's mm:ss.MM format.
	hour = int(time[:-10])
	minute = int(time[3:-7])
	sec = int(time[6:-4])
	msec = (int(time[9:-1]))
	
	if hour > 0:
		for x in range (0, hour):
			minute += 60
	
	output = ''
	
	if minute < 10:
		output = output + '0'
	output = output + str(minute) + ':'
	if sec < 10:
		output = output + '0'
	output = output + str(sec) + '.'
	if msec < 10:
		output = output + '0'
	return output + str(msec)

def second_subtract(time1, time2):
# Calculates the duration the comment needs to be on-screen and outputs in units of seconds.
# Accepts input in SRT hh:mm:ss,MMM string format. time1 is the initial time and time2 is when the comment should end.
	time1r = time_reparser(time1)
	time2r = time_reparser(time2)
	minute = int(time2r[:-6]) - int(time1r[:-6])
	sec = int(time2r[3:-3]) - int(time1r[3:-3])
	msec = int(time2r[6:]) - (int(time1r[6:]))
	
	if minute < 0:
		return ''
	elif minute > 0:
		for x in range (0, minute):
			sec += 60
			
	if msec < 0:
		sec -= 1
		msec = 100 + msec
	
	if sec < 0:
		return ''
	
	if msec < 10:
		return str(sec) + '.0' + str(msec)
	else:
		return str(sec) + '.' +  str(msec)

def output_generator(start, duration, comment):
# Takes in properly formatted inputs for the three NicoScript fields and generates a NicoScript-formatted block for it.
	if comment == '':
		return ''
	else:
		return ' {\r\n  \"time\": \"' + start + '\",\r\n  \"command\": \"@' + duration + ' shita small\",\r\n  \"comment\": \"' + comment + '\"\r\n },\r\n'

def input_parse(input):
#Parses an SRT block string into individual components and reassembles them.
	components = re.split('\r\n', input.group())
	times = re.split(' --> ', components[1])
	
	start = time_reparser(times[0])
	duration = second_subtract(times[0], times[1])

# Collects all of the lines of text in the original SRT block and outputs NicoScript-formatted blocks in reverse order.
	outstring = ''
	for x in components[2:]:
		outstring = output_generator(start, duration, x) + outstring
	return outstring
	

# Ensure that all newlines show up as carriage returns
editor.rereplace(r'([^\r])\n', r'\1\r\n')
# Actual replacement of core subtitle sections
editor.rereplace(r'[0-9]*\r\n[0-9][0-9]:([0-9][0-9]:[0-9][0-9],[0-9][0-9])[0-9] --> 00:([0-9][0-9]:[0-9][0-9],[0-9][0-9])[0-9]\r\n([^\r\n]+\r\n)*\r\n', input_parse)
# Addition of outer brackets
editor.insertText(0, '[\r\n')
editor.appendText(']')
# Cleaning up loose ends to prevent syntax errors
editor.rereplace(r',[\r\n]*\]', '\r\n\]')
