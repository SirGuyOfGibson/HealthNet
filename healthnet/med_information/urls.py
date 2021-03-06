from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^result/create/$', views.createTestResult, name='create_test_result'),
    url(r'^record/create/$', views.createRecord, name='create_record'),
    url(r'^prescription/create/$', views.createPrescription, name='create_prescription'),
    url(r'^prescription/create/(?P<patientid>[0-9]+)$', views.createPrescription, name='create_prescription'),
    url(r'^prescription/update/(?P<prescriptionid>[0-9]+)/$', views.updatePrescription, name='update_prescription'),
    url(r'^prescription/view/(?P<patientid>[0-9]+)/$', views.viewPrescription, name='view_prescription'),
    url(r'^prescription/view/$', views.viewPrescription, name='view_prescription')
]
