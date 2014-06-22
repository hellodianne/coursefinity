import os

def populate():
	add_link(title="make website a day for 180 days", url="http://jenniferdewalt.com/")
	add_link(title="How I taught myself to code in 8 weeks", url="http://tech.yipit.com/2012/08/21/how-i-taught-myself-to-code-in-8-weeks/")
	add_link(title="How can I find my first job as a web developer", url="https://blog.sortiq.com/how-can-i-find-my-first-job-as-a-web-developer/")
	add_link(title="I got a job", url="http://www.reddit.com/r/learnpython/comments/1gzs2e/i_got_a_job_oh_f_i_got_a_job/")
	add_link(title="Making game development a career", url="http://markckim.blogspot.com/2013/03/making-game-development-career.html")

	#print out what we have added
	for c in Link.objects.all():
		print str(c)

def add_link(title, url):
	article = Link.objects.get_or_create(title=title, url=url)[0]
	return article

#Start execution

if __name__ == '__main__':
	print "Starting population script for links"
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coursefinityProject.settings')
	from coursefinity.models import Link
	populate()