from django.urls import path
from rest_framework import  routers
from django.urls import  include, path
from .views import AppointmentViewSet, DoctorViewSet, PatientViewSet, ReservationViewSet, PersonaldataViewSet

router = routers.DefaultRouter()
router.register(r'Appointment', AppointmentViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'personaldatas', PersonaldataViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]