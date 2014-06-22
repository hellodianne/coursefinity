from django.db import models

#Model for articles under inspiration
#manipulate in admin
class Link(models.Model):
	title = models.CharField(max_length = 128)
	url = models.URLField(max_length=250)


	def __unicode__(self):
		return self.title

class Career(models.Model):
	name = models.CharField(max_length = 128)
	body = models.TextField(null = True, blank = True)

	def __unicode__(self):
		return self.name

class Program(models.Model):
	career = models.ForeignKey(Career) 
	name = models.CharField(max_length=128)

	def __unicode__(self):
		return self.name

class Courses(models.Model):
	program = models.ForeignKey(Program)
	title = models.CharField(max_length = 128)
	url = models.URLField()
	description = models.CharField(max_length=250, null=True, blank=True)
	
	def __unicode__(self):
		return self.title



