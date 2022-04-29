# Generated by Django 4.0.2 on 2022-02-27 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notiteApp', '0002_remove_note_pub_date_note_created_at_note_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='importance',
            field=models.IntegerField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], default=3),
        ),
    ]
