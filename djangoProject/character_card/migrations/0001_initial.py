# Generated by Django 4.2.6 on 2023-12-04 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('race', models.TextField()),
                ('class_name', models.TextField(db_column='class')),
                ('level', models.IntegerField()),
                ('strength', models.IntegerField()),
                ('dexterity', models.IntegerField()),
                ('constitution', models.IntegerField()),
                ('intelligence', models.IntegerField()),
                ('wisdom', models.IntegerField()),
                ('charisma', models.IntegerField()),
                ('StrST', models.IntegerField()),
                ('DexST', models.IntegerField()),
                ('ConST', models.IntegerField()),
                ('IntST', models.IntegerField()),
                ('WisST', models.IntegerField()),
                ('Mhitdice', models.IntegerField()),
                ('Chitdice', models.IntegerField()),
                ('Dsp', models.IntegerField()),
                ('Dsf', models.IntegerField()),
                ('skills', models.TextField()),
                ('proficiencies', models.TextField()),
                ('spells', models.TextField()),
                ('inventory', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
