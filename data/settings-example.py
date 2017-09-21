# if you want to override the default settings, rename this to settings.py
# all preferences must be present or none will be overridden

# boolean determining if you want to have the script adjust the temp returned
# to account for the temp of the RPi CPU
adjusttemp = True

# amount of time between sensor readings (in minutes)
readingdelta = 2

# if True activates a thread to monitor the SenseHAT Joystick and convert those inputs
# into key presses (useful to control Kodi using the Joystick)
convertjoystick = True