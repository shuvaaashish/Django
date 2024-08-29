from django.urls import path
from . import views
urlpatterns=[
    path("", views.index , name="index"),
    path("shuva", views.shuva , name="shuva"),
    path("<str:name>", views.greet , name="greet")
]