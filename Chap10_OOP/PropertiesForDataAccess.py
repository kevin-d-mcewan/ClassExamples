#PropertiesForDataAccess.py

from timewithproperties import Time

""" Create a TIME obj. TIME's __init__ method has HOUR, MIN and
SECOND params, each w/default value of 0."""
# Here, specify the HR and MIN-SEC def to 0:

wake_up = Time(hour=6, minute=30)

print(wake_up)
print('----------------------------------------------')

print(wake_up.__repr__)         # Print using __repr__ method
print(wake_up.__str__)          # Print using __str__ method
print('----------------------------------------------')

print(str(wake_up))             # RightWay print using __str__
print(repr(wake_up))            # RightWay Print using __repr__ method
print('----------------------------------------------')

# GETTING AN ATTR VIA A PROPERTY
print("wake_up.hour = ", wake_up.hour)
# OR
print("wake_up.hour = " + str(wake_up.hour))
print('---------------------------------------------')

""" SETTING THE TIME """
wake_up.set_time(hour = 7, minute = 40)
print(wake_up)
print('OR...')
print(repr(wake_up))
print('------------------------------------------------')


# SETTING AN ATTR VIA A PROPERTY
wake_up.hour = 8
print(wake_up)
print('OR...')
print(repr(wake_up))
print('===============================================')

''' ATTEMPTING TO SET AN INVALID VALUE'''
# wake_up.hour = 100
print(wake_up)
print('-------------------------------')

wake_up = Time(hour=7, minute=23, second=14)
print(str(wake_up.hour))
print(wake_up.hour)
print('-----------------------------------')











