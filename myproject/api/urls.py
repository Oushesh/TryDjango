'''
The urls.py expose the endpoint
'''

from django.urls import path
from . import views

#path always take the 'url' string and views data

urlpatterns = [path('',views.getData),
			   path('add/',views.addItem)
			   ]


