# Generated by Django 3.1.7 on 2021-02-22 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holy', '0003_auto_20210222_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='SIGN_UP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.TextField(max_length=10, null=True)),
                ('f_name', models.TextField(max_length=10, null=True)),
                ('l_name', models.TextField(max_length=10, null=True)),
                ('e_mail', models.EmailField(max_length=10, null=True)),
                ('cont', models.IntegerField(null=True)),
                ('pwd', models.TextField(null=True)),
            ],
        ),
    ]
