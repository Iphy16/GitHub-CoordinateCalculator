

##-------------------------------------------------------------------------------------
## Name:  CoordinateCalculator.py
## Description:  Converts geographic coordinates in DDMMSS format to DD
## Created:  Sept 04, 2024
## Author:  Ifeoma F. Okonye (ifokonye@ksu.edu)
##-------------------------------------------------------------------------------------


## Request user-coordinates in DDMMSS format (note streing format)
x = input("Please enter a corrdinate values in DDDMMSS format: ")

# Convert to seconds to minutes
ss = int(x[-2:]) / 60

# Add converted seconds to minutes and convert to degrees
mm = (int(x[-4:-2:]) + ss) / 60

# Add converted minutes to degrees
dd = int(x[:2]) + mm

# Print the final result as a friendly message
print("Your new coordinate in decimal degrees is {0}".format(str(round(dd, 2))))









