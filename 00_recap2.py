

class TheMain:
	name = 'Main'
	status = 'Sir'

	def get_name(self):
		return self.name

	def get_status(self):
		return self.status

	def get_full_name(self):
		return self.get_status() + ' ' + self.get_name()



class Student(TheMain):
	def __init__(self, name):
		self.__name = name

	def get_name(self):
		return self.__name


main = TheMain()
print(main.get_full_name())

alex = Student('Alex')
print(alex.get_full_name())