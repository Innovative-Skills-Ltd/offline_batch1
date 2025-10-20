"""
URL configuration for off_demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views as demo_view

from . import views1 as v
from .views1 import HomeView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


def home_view(request):
    view = HomeView()
    return view.get1(request)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('demo/',demo_view.demo_function),
    # path('demo/show/',demo_view.show)
    # path('', v.demo),
    # path('home/', home_view, name='home'),
    # path('myapp/', include('demoapp1.urls')),
    path('demo/',demo_view.demo_function1),
    path('demo_course/',demo_view.course),
    path('insert/',demo_view.customer,name='customer_insert'),
    path('course/insert/',demo_view.course_insert,name='course_insert'),
    path('update/',demo_view.customer_update,name='customer_update'),

    path('demo/show',demo_view.demo_function_show,name='show_customer'),
    path('course/show',demo_view.course_show,name='show_course'),
    path('demo/edit/<int:id>/',demo_view.edit,name='data_edit')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print(urlpatterns)