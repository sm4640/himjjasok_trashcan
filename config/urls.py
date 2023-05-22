"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from advices.views import start_page, letter, trash_can, cookie1, cookie2, last_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start_page),
    path('letter', letter, name = 'letter_page'),
    path('trashcan', trash_can, name = 'trashcan_page'),
    path('cookie1', cookie1, name = 'cookie1_page'),
    path('cookie2', cookie2, name = 'cookie2_page'),
    path('lastpage', last_page, name = 'last_page'),
    #path('advices/advice', give_advice, name = 'give_advice'),
    #path('advices/advice_2', real_advice),
]
