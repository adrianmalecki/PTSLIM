from django.urls import path
from rest_framework import  routers
from django.urls import  include, path
from django.conf.urls import url
from .views import CreatePersonalDataView, PersonalDataDetailsView, CreatePatientView, CreateDoctorView, \
    CreateReservationView, PatientDetailsView, DoctorDetailsView, ReservationDetailsView

urlpatterns = [
    url(r'^personaldata/$', CreatePersonalDataView.as_view(), name="create"),
    url(r'^personaldata/(?P<pk>[0-9]+)/$', PersonalDataDetailsView.as_view(), name="details"),

    url(r'^personaldata/$', CreatePatientView.as_view(), name="create"),
    url(r'^personaldata/(?P<pk>[0-9]+)/$', PatientDetailsView.as_view(), name="details"),

    url(r'^personaldata/$', CreateDoctorView.as_view(), name="create"),
    url(r'^personaldata/(?P<pk>[0-9]+)/$', DoctorDetailsView.as_view(), name="details"),

    url(r'^personaldata/$', CreateReservationView.as_view(), name="create"),
    url(r'^personaldata/(?P<pk>[0-9]+)/$', ReservationDetailsView.as_view(), name="details"),
]