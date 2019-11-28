def function1():
	function2()


def function2():
	raise Exception('An exception occurred')


# function1()
'''Calling function1() causes a TRACEBACK Exception to occur'''

