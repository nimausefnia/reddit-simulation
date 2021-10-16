from django.urls import path,include
from . import views
from . import api_views



api_url=[
    path('question/list/',api_views.QuestionListView.as_view()),
    path('question/create/',api_views.QuestionCreateView.as_view()),
    path('question/<int:pk>/',api_views.QuestionUpdateView.as_view()),
    path('question/<int:pk>/',api_views.QuestionDeleteView.as_view()),
    path('answer/<int:pk>/',api_views.AnswerDeleteView.as_view()),
    path('answer/create/',api_views.AnswerCreateView.as_view()),
    path('answer/update/<int:pk>/',api_views.AnswerUpdateView.as_view()),





]








app_name='core'
urlpatterns=[
    path('', views.Home.as_view(), name='home'),
    path('api/', include(api_url)),

]