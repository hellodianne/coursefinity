import os

#career - program - courses
#writer - academic writing - tech writing fr different sites a, b, c
#career name, body
#program career, name
#courses program, title, url, description

def populate():
	writer_career = add_career('Writer', """Lorem ipsum dolor sit amet, consectetuer 
		adipiscing elit. Aenean commodo ligula eget dolor. 
		Aenean massa. Cum sociis natoque penatibus et magnis 
		dis parturient montes, nascetur ridiculus mus. Donec quam felis, 
		ultricies nec, pellentesque eu, pretium quis, sem. 
		Nulla consequat massa quis enim. Donec pede justo, 
		fringilla vel, aliquet nec, vulputate eget, arcu.""")

	writer_prog = add_program(career = writer_career, nam = "English Grammar")

	add_course(prog = writer_prog, 
		title = "How to Think like a Computer Mathematecian",
		url = "http://www.greenteapress.com/thinkpython/",
		description = """Cum sociis natoque penatibus et magnis 
		dis parturient montes, nascetur ridiculus mus. Donec quam felis, 
		ultricies nec, pellentesque eu, pretium quis,""")

	add_course(prog = writer_prog, 
		title = "How to Think like a Computer Grammarian",
		url = "http://www.greenteapress.com/thinkpython/",
		description = """Cum sociis natoque penatibus et magnis 
		dis parturient montes, nascetur ridiculus mus. Donec quam felis, 
		ultricies nec, pellentesque eu, pretium quis,""")

	add_course(prog = writer_prog, 
		title = "How to Think like a Computer Agent",
		url = "http://www.greenteapress.com/thinkpython/",
		description = """Cum sociis natoque penatibus et magnis 
		dis parturient montes, nascetur ridiculus mus. Donec quam felis, 
		ultricies nec, pellentesque eu, pretium quis,""")

	developer_career = add_career('Developer', """Lorem ipsum dolor sit amet, consectetuer 
		adipiscing elit. Aenean commodo ligula eget dolor. 
		Aenean massa. Cum sociis natoque penatibus et magnis 
		dis parturient montes, nascetur ridiculus mus. Donec quam felis, 
		ultricies nec, pellentesque eu, pretium quis, sem. 
		Nulla consequat massa quis enim. Donec pede justo, 
		fringilla vel, aliquet nec, vulputate eget, arcu.""")

	dev_prog = add_program(career = developer_career, 
		nam = "Software Engineering")

	add_course(prog = dev_prog, 
		title = "How to Think like a Computer Mathematecian",
		url = "http://www.greenteapress.com/thinkpython/",
		description = """Cum sociis natoque penatibus et magnis
		dis parturient montes, nascetur ridiculus mus. Donec quam felis, 
		ultricies nec, pellentesque eu, pretium quis,""")

	add_course(prog = dev_prog, 
		title = "How to Think like a Computer Grammarian",
		url = "http://www.greenteapress.com/thinkpython/",
		description = """Cum sociis natoque penatibus et magnis 
		dis parturient montes, nascetur ridiculus mus. Donec quam felis, 
		ultricies nec, pellentesque eu, pretium quis,""")

	add_course(prog = dev_prog, 
		title = "How to Think like a Computer Agent",
		url = "http://www.greenteapress.com/thinkpython/",
		description = """Cum sociis natoque penatibus et magnis 
		dis parturient montes, nascetur ridiculus mus. Donec quam felis, 
		ultricies nec, pellentesque eu, pretium quis,""")
#add career
def add_course(prog, title, url, description):
	c = Courses.objects.get_or_create(prog=prog, title=title, url=url, description=description)
	return c 

def add_program(career, nam):
	p = Program.objects.get_or_create(career=career, name=nam)

def add_career(name, body):
	c = Career.objects.get_or_create(name=name, body=body)
	return c





if __name__ == '__main__':
	print "Starting CareerProgram population script"
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coursefinityProject.settings')
	from coursefinity.models import Career, Program, Courses
	populate()




