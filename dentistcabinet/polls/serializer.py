from .models import Appointment, Doctor, Patient, Personaldata, Reservation
from rest_framework import serializers

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['appointmentid','patientid','doctorid','reservationid','starttime', 'endtime','cabinetnumber','comments']


class PersonaldataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personaldata
        fields = ['personaldataid','firstname','lastname','phone','email']


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = ['reservationid', 'patientid', 'doctorid', 'starttime', 'endtime']


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['patientid','personaldataid','insurancenumber']


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['doctorid', 'personaldataid', 'specialization']
