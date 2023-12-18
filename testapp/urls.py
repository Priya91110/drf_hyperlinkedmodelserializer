
from django.contrib import admin
from django.urls import path, include
from testapp.views import StudentListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('studentdata',StudentListView,basename="student")


urlpatterns = [
    path('',include(router.urls)),
]
