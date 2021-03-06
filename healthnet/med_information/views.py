from django.contrib.auth.decorators import login_required, permission_required
from django.db import transaction
from django.shortcuts import render, redirect

from .models.prescription import PrescriptionForm, Prescription
from django.contrib import messages
from .models.result import Result, ResultForm
from .models.record import Record, RecordForm
from users.models.person import Doctor, Patient

def createPrescription(request, patientid=None):
    if request.method == 'POST':
        prescription_form = PrescriptionForm(request.POST)

        if prescription_form.is_valid():
            prescription = prescription_form.save()
            if request.user.person.is_doctor:
                prescription.doctor = Doctor.objects.get(id=request.user.person.id)
            if patientid is not None:
                prescription.patient = Patient.objects.get(id=patientid)
            prescription.save()
        else:
            print('we have an error')

        return redirect('view_prescription', patientid=patientid)

    else:
        prescription_form = PrescriptionForm()
        if patientid is not None:
            del prescription_form.fields['patient']
        return render(request, 'med_information/prescription.html', {'PrescriptionForm':prescription_form})

@login_required
@transaction.atomic
def updatePrescription(request, prescriptionid):
    if request.method == 'POST':
        prescription_form = PrescriptionForm(request.POST)
        del prescription_form.fields['startDate']

        if prescription_form.is_valid():
            prescription = Prescription.objects.get(id=prescriptionid)
            if request.user.person.is_doctor:
                prescription.title = prescription_form.cleaned_data['title']
                prescription.duration = prescription_form.cleaned_data['duration']
                prescription.instructions = prescription_form.cleaned_data['instructions']
                prescription.save()
                messages.success(request, "Prescription Updated!")
                return redirect('view_prescription', patientid=prescription.patient.id)
        else:
            print('houston we have an error')
    else:
        prescription_form = PrescriptionForm(instance=Prescription.objects.get(id=prescriptionid))
        del prescription_form.fields['startDate']


    return render(request, 'med_information/prescription.html', {'prescriptionForm':prescription_form, 'prescriptionid':prescriptionid})


@login_required
@transaction.atomic
def viewPrescription(request, patientid=None):
    if patientid is not None:
        patient = Patient.objects.get(id = patientid)
    else:
        patient = Patient.objects.get(user = request.user)

    prescriptions = Prescription.objects.filter(patient=patient)

    return render(request, 'med_information/viewPrescriptions.html', {'prescriptions':prescriptions, 'patient':patient})

def createTestResult(request):
    if request.method == 'POST':
        result_form = ResultForm(request.POST)

        if result_form.is_valid():
            result = result_form.save()
            result.doctor = Doctor.objects.get( id=request.user.person.id )
            result.save()
            return redirect('admitted_patients')

    elif request.method == 'GET':
        result_form = ResultForm()

    return render(request, 'med_information/result.html', {'result_form':result_form})

def createRecord(request):
    if request.method == 'POST':
        record_form = RecordForm(request.POST)

        if record_form.is_valid():
            record = record_form.save()
            record.doctor = Doctor.objects.get(id=request.user.person.id)
            record.save()
            return redirect('admitted_patients')

    elif request.method == 'GET':
        record_form = RecordForm()

    return render(request, 'med_information/record.html', {'record_form': record_form})

