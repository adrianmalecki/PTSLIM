from django.http import HttpResponse
from .models import Appointment, Doctor, Patient, Personaldata, Reservation
from rest_framework import viewsets
from .serializer import AppointmentSerializer, DoctorSerializer, PatientSerializer, ReservationSerializer, PersonaldataSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PersonaldataViewSet(viewsets.ModelViewSet):
    queryset = Personaldata.objects.all()
    serializer_class = PersonaldataSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
