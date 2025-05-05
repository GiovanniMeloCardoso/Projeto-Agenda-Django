from django.urls import path
from contact import views

app_name = 'contact'
# The app_name is used to create namespaced URLs for the app.
#  This is useful when you have multiple apps in your project and want to avoid URL name conflicts.

urlpatterns = [
    path('', views.index, name='index'),
]