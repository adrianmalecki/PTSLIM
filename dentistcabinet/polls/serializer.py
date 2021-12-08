from .models import Doctor, Patient, Personaldata, Reservation
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class PersonaldataSerializer(serializers.ModelSerializer):
    class Meta:
        password = serializers.CharField(write_only=True)
        model = Personaldata
        fields = ['personaldataid', 'firstname', 'lastname', 'phone', 'email', 'password']
        write_only_fields = ('password',)
        read_only_fields = ('personaldataid',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validated_data):
            personaldata = Personaldata.objects.create(
                personaldataid=Personaldata.objects.all().count() + 1,
                email=validated_data['email'],
                firstname=validated_data['firstname'],
                lastname=validated_data['lastname'],
                phone=validated_data['phone'],
            )

            # personaldata.set_password(validated_data['password'])
            personaldata.save()

            return personaldata

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['patientid', 'personaldataid', 'personaldatas']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['reservationid', 'patientid', 'doctorid', 'starttime', 'endtime', 'cabinetnumber', 'comments']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['doctorid', 'personaldataid', 'specialization']


'''
class PersonaldataSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Personaldata
        fields = ['personaldataid','firstname','lastname','phone','email', 'password']
        write_only_fields = ('password',)
        read_only_fields = ('personaldataid',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        personaldata = Personaldata.objects.create(
            personaldataid=Personaldata.objects.all().count()+1,
            email=validated_data['email'],
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'],
            phone=validated_data['phone'],
        )

        #personaldata.set_password(validated_data['password'])
        personaldata.save()

        return personaldata

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance
    
    

class PatientSerializer(serializers.ModelSerializer):

    personaldatas = serializers.PrimaryKeyRelatedField(queryset=Personaldata.objects.all())

    class Meta:
        model = Patient
        fields = ['patientid','personaldataid','personaldatas']
        write_only_fields = ('password',)
        read_only_fields = ('patientid','personaldataid',)
        #fields = ['patientid', 'personaldataid', 'insurancenumber']

    def create(self, validated_data):
        patient = Patient.objects.create(
            patientid=Patient.objects.all().count() + 1,
            personaldataid=Personaldata.objects.all().count() + 1,
            email=validated_data['email'],
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'],
            phone=validated_data['phone'],
            insurancenumber=validated_data['insurancenumber'],
    )
        patient.save()

        return patient

    def update(self, instance, validated_data):
        instance.insurancenumber = validated_data.get('insurancenumber', instance.insurancenumber)
        instance.email = validated_data.get('email', instance.email)
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance
'''
