from django.urls import path
from  . import views
app_name='NER'
urlpatterns=[
    path('',views.token_text)
]
