from django.urls import path
from . import views
# url can be custom whatever you want
# but you must use url href in xxx.html like {% url 'viewname' view_params%}

# namespace
app_name = "poll"
# common define
# urlpatterns = [
# 	#ex: /poll/
# 	path('',views.index,name="index"),
# 	path('specifics/<int:question_id>/',views.detail,name="detail"),
# 	path('<int:question_id>/results',views.results,name="results"),
# 	path('<int:question_id>/vote',views.vote,name="vote"),

# ]

# use generic view system to define view
urlpatterns = [
 	path('',views.IndexView.as_view(),name="index"),
	path('specifics/<int:pk>/',views.DetailView.as_view(),name="detail"),
 	path('<int:pk>/results',views.ResultsView.as_view(),name="results"),
 	path('<int:question_id>/vote',views.vote,name="vote"),
]