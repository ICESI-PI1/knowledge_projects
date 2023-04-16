# Generated by Django 4.1.7 on 2023-04-03 18:18

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_convocatory_projectid_remove_employee_role_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Binnacle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('binnacleId', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nit', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('adress', models.CharField(max_length=20)),
                ('representativeName', models.TextField()),
                ('phoneNumberRepresentative', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('projectId', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('result', models.TextField()),
                ('scope', models.TextField()),
                ('workPlan', models.TextField()),
                ('budget', models.DecimalField(decimal_places=0, max_digits=10)),
                ('humanCapital', models.TextField()),
                ('state', models.CharField(max_length=20)),
                ('goal', models.TextField()),
                ('asssignedResources', models.TextField()),
                ('category', models.CharField(max_length=20)),
                ('convocatoryNumber', models.IntegerField()),
                ('nit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logId', models.CharField(max_length=10)),
                ('dateTime', models.DateTimeField()),
                ('observations', models.TextField()),
                ('results', models.TextField()),
                ('binnacleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.binnacle')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('fullName', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
                ('birthDate', models.DateField()),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Convocatory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('convocatoryId', models.CharField(max_length=5)),
                ('startDate', models.DateField()),
                ('closingDate', models.DateField()),
                ('projectId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.project')),
            ],
        ),
        migrations.AddField(
            model_name='binnacle',
            name='projectId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.project'),
        ),
    ]
