from django.urls import path
from .views import SubredsView, SubredView

app_name= 'subs'

urlpatterns = [
 path('subs/', SubredsView.as_view(), name='subred'),
 path('subs/<slug:slug>/', SubredView.as_view(), name='subreds'),
  ]
