"""Define urls for learning log"""
from django.urls import path
from . import views
app_name = 'learning_logs'
urlpatterns = [
		# Home page
		path('', views.index, name='index'),
		path('topics/', views.topics, name='topics'),
		# Detailed page for topics
		path('topics/<int:topic_id>/', views.topic, name='topic'),
		# Page to add new topic
		path('new_topic/', views.new_topic, name ='new_topic'),
		#Page for adding a new entry
		path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
		#Page for editing entrys
		path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]