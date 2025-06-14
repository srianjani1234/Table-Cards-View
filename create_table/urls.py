from django.urls import path
from.import views
urlpatterns=[
  path('',views.table,name="table"),
  path('2',views.cards,name="cards")
 
]