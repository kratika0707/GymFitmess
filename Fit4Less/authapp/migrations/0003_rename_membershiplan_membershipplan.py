# Generated by Django 4.1.7 on 2023-03-31 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_enrollment_membershiplan_trainer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MembershiPlan',
            new_name='MembershipPlan',
        ),
    ]
