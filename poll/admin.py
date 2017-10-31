from django.contrib import admin
from .models import Question,Choice
# Register your models here.
# customize the admin form

class ChoiceInline(admin.TabularInline):
	# TabularInline - horiziontal
	# StackedInline - vertical
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	#change fields order
	#fields = ['pub_date','question_text']
	# add fileds title
	fieldsets = [
		("Question info",{"fields":['question_text']}),
		("Date info",{"fields":['pub_date']})
	]
	# when show question detail.also can edit choice for
	inlines = [ChoiceInline]
	# customize -------
	list_display = ('question_text','pub_date','was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)
