# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 02:19
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.management import create_permissions

nurseNames = [
'kathleen',
'pamela',
'martha',
'debra',
'amanda',
'stephanie',
'carolyn',
'christine',
'marie',
'janet',
]

doctorNames = [
'mary',
'patricia',
'linda',
'barbara',
'elizabeth',
'jennifer',
'maria',
]
adminNames = [
'margaret',
'dorothy',
'lisa',
'nancy',
'karen',
'betty',
'helen',
'sandra',
'donna',
'carol',
'ruth',
'sharon',
'michelle',
]
patientNames = [
'laura',
'sarah',
'kimberly',
'deborah',
'jessica',
'shirley',
'cynthia',
'angela',
'melissa',
'brenda',
'amy',
'anna',
'rebecca',
'virginia',
]

def create_users(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    User = apps.get_model('auth','User')
    for user in patientNames:
        User.objects.using(db_alias).create(username=user, password="pbkdf2_sha256$36000$sPr6g8qk2ghI$4WRKCYwkafGcJSnPWbfEq4ePEF8L9CkdTJEaF+s7dfM=")
    for user in adminNames:
        User.objects.using(db_alias).create(username=user, password="pbkdf2_sha256$36000$sPr6g8qk2ghI$4WRKCYwkafGcJSnPWbfEq4ePEF8L9CkdTJEaF+s7dfM=")
    for user in doctorNames:
        User.objects.using(db_alias).create(username=user, password="pbkdf2_sha256$36000$sPr6g8qk2ghI$4WRKCYwkafGcJSnPWbfEq4ePEF8L9CkdTJEaF+s7dfM=")
    for user in nurseNames:
        User.objects.using(db_alias).create(username=user, password="pbkdf2_sha256$36000$sPr6g8qk2ghI$4WRKCYwkafGcJSnPWbfEq4ePEF8L9CkdTJEaF+s7dfM=")

def delete_users(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    User = apps.get_model('auth','User')
    User.objects.using(db_alias).all().delete()

def create_people(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Person = apps.get_model('users', 'Person')
    Person.objects.using(db_alias).all().delete()

    Hospital = apps.get_model('users', 'Hospital')
    uor = Hospital.objects.using(db_alias).get(name="UoR Hospital")
    strong = Hospital.objects.using(db_alias).get(name="Strong Memorial Hospital")

    for name in adminNames:
        Admin = apps.get_model('users', 'Admin')
        user = User.objects.using(db_alias).get(username=name)
        hospital = uor
        if((user.id % 2) == 0):
            hospital = strong
        Admin.objects.using(db_alias).create(name=name, is_admin=True,
                                             user_id=user.id,
                                             hospital=hospital)
        admin = Admin.objects.using(db_alias).get(name=name)
        content_type = ContentType.objects.get_for_model(apps.get_model('users', 'Patient'))
        permission = Permission.objects.get(
            codename='update_patient',
            content_type=content_type,
        )
        admin.user.user_permissions.add(permission.id)
        content_type = ContentType.objects.get_for_model(apps.get_model('users', 'Admin'))
        permission = Permission.objects.get(
            codename='update',
            content_type=content_type,
        )
        admin.user.user_permissions.add(permission.id)
        permission = Permission.objects.get(
            codename='transfer',
            content_type=content_type,
        )
        admin.user.user_permissions.add(permission.id)
        permission = Permission.objects.get(
            codename='logs',
            content_type=content_type,
        )
        admin.user.user_permissions.add(permission.id)
        admin.save()

    for name in patientNames:
        Patient = apps.get_model('users', 'Patient')
        user = User.objects.using(db_alias).get(username=name)
        hospital = uor
        if((user.id % 2) == 0):
            hospital = strong
        Patient.objects.using(db_alias).create(name=name, is_patient=True,
                                               user_id=user.id,
                                               hospital=hospital)
        patient = Patient.objects.using(db_alias).get(user_id=user.id)
        content_type = ContentType.objects.get_for_model(Patient)
        permission = Permission.objects.get(
            codename='update_patient',
            content_type=content_type,
        )
        patient.user.user_permissions.add(permission.id)
        permission = Permission.objects.get(
            codename='update',
            content_type=content_type,
        )
        patient.user.user_permissions.add(permission.id)

    for name in doctorNames:
        Doctor = apps.get_model('users', 'Doctor')
        user = User.objects.using(db_alias).get(username=name)

        hospital = uor
        if((user.id % 2) == 0):
            hospital = strong
        Doctor.objects.using(db_alias).create(name=name, is_doctor=True,
                                              user_id=user.id,
                                              hospital=hospital)
        doctor = Doctor.objects.using(db_alias).get(user_id=user.id)

        content_type = ContentType.objects.get_for_model(apps.get_model('users', 'Doctor'))
        permission = Permission.objects.get(
            codename='admit',
            content_type=content_type,
        )
        doctor.user.user_permissions.add(permission.id)
        content_type = ContentType.objects.get_for_model(apps.get_model('users', 'Doctor'))
        permission = Permission.objects.get(
            codename='release',
            content_type=content_type,
        )
        doctor.user.user_permissions.add(permission.id)
        content_type = ContentType.objects.get_for_model(apps.get_model('users', 'Doctor'))
        permission = Permission.objects.get(
            codename='view_cal',
            content_type=content_type,
        )
        doctor.user.user_permissions.add(permission.id)
        doctor.save()

    for name in nurseNames:
        Nurse = apps.get_model('users', 'Nurse')
        user = User.objects.using(db_alias).get(username=name)

        hospital = uor
        if((user.id % 2) == 0):
            hospital = strong
        Nurse.objects.using(db_alias).create(name=name, is_nurse=True,
                                             user_id=user.id,
                                             hospital=hospital)
        nurse = Nurse.objects.using(db_alias).get(user_id=user.id)
        content_type = ContentType.objects.get_for_model(apps.get_model('users', 'Doctor'))
        permission = Permission.objects.get(
            codename='admit',
            content_type=content_type,
        )
        nurse.user.user_permissions.add(permission.id)
        content_type = ContentType.objects.get_for_model(apps.get_model('users', 'Doctor'))
        permission = Permission.objects.get(
            codename='release',
            content_type=content_type,
        )
        nurse.user.user_permissions.add(permission.id)
        content_type = ContentType.objects.get_for_model(apps.get_model('users', 'Doctor'))
        permission = Permission.objects.get(
            codename='view_cal',
            content_type=content_type,
        )
        nurse.user.user_permissions.add(permission.id)
        nurse.save()

def delete_people(apps, schema_editor):
    db_alias = schema_editor.connection.alias

    Admin = apps.get_model('users', 'Admin')
    Doctor = apps.get_model('users', 'Doctor')
    Patient = apps.get_model('users', 'Patient')
    Nurse = apps.get_model('users', 'Nurse')

    Admin.objects.using(db_alias).all().delete()
    Doctor.objects.using(db_alias).all().delete()
    Patient.objects.using(db_alias).all().delete()
    Nurse.objects.using(db_alias).all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170717_2122'),
    ]

    operations = [
        migrations.RunPython(create_users,  delete_users),
        migrations.RunPython(create_people, delete_people),
    ]
