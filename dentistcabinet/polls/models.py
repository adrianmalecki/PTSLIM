from django.db import models

class Reservation(models.Model):
    reservationid = models.IntegerField(db_column='ReservationID', primary_key=True)  # Field name made lowercase.
    patientid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='PatientID', blank=True, null=True)  # Field name made lowercase.
    doctorid = models.ForeignKey('Doctor', models.DO_NOTHING, db_column='DoctorID', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    cabinetnumber = models.IntegerField(db_column='CabinetNumber', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Appointment'


class Doctor(models.Model):
    doctorid = models.IntegerField(db_column='DoctorID', primary_key=True)  # Field name made lowercase.
    personaldataid = models.ForeignKey('Personaldata', models.DO_NOTHING, db_column='PersonalDataID', blank=True, null=True)  # Field name made lowercase.
    specialization = models.TextField(db_column='Specialization', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Doctor'


class Patient(models.Model):
    patientid = models.IntegerField(db_column='PatientID', primary_key=True)  # Field name made lowercase.
    personaldataid = models.ForeignKey('Personaldata', models.DO_NOTHING, db_column='PersonalDataID', blank=True, null=True)  # Field name made lowercase.
    insurancenumber = models.TextField(db_column='InsuranceNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Patient'


class Personaldata(models.Model):
    personaldataid = models.IntegerField(db_column='PersonalDataID', primary_key=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName', blank=True, null=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PersonalData'
