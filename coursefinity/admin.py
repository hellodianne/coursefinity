from django.contrib import admin
from coursefinity.models import Link, Career, Program, Courses

class LinkAdmin(admin.ModelAdmin):
	pass

class CareerAdmin(admin.ModelAdmin):
	list_display= ('name', 'body')

class ProgramAdmin(admin.ModelAdmin):
	fields = ['career', 'name']
	list_display = ('get_career',)

	def get_career(self, obj):
		return "\n".join([c.name for c in obj.career.all()])


class CoursesAdmin(admin.ModelAdmin):
	list_display = ('program', 'title', 'url', 'description')

admin.site.register(Link, LinkAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Courses, CoursesAdmin)

