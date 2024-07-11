# Generated by Django 4.2.6 on 2024-07-09 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0004_auto_20240708_1511"),
        ("company", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="employees",
            field=models.ManyToManyField(
                related_name="company_employees", to="employees.employee"
            ),
        ),
        migrations.DeleteModel(
            name="Employee",
        ),
    ]