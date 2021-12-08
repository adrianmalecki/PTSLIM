from django.http import HttpResponse
from .models import Doctor, Patient, Personaldata, Reservation
from rest_framework import viewsets, generics, permissions
from .serializer import DoctorSerializer, PatientSerializer, ReservationSerializer, \
    PersonaldataSerializer
from rest_framework.permissions import AllowAny



class CreatePersonalDataView(generics.ListCreateAPIView):
    queryset = Personaldata.objects.all()
    serializer_class = PersonaldataSerializer
    #permission_classes = (permissions.IsAuthenticated, IsOwner))


class PersonalDataDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personaldata.objects.all()
    serializer_class = PersonaldataSerializer
    #permission_classes = (permissions.IsAuthenticated, IsOwner))


class CreatePatientView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    #permission_classes = (permissions.IsAuthenticated, IsOwner))


class PatientDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    #permission_classes = (permissions.IsAuthenticated, IsOwner))


class CreateDoctorView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    #permission_classes = (permissions.IsAuthenticated, IsOwner))


class DoctorDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    #permission_classes = (permissions.IsAuthenticated, IsOwner))

class CreateReservationView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    #permission_classes = (permissions.IsAuthenticated, IsOwner))


class ReservationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    #permission_classes = (permissions.IsAuthenticated, IsOwner))
