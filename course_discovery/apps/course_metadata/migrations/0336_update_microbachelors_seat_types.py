"""
Migration to remove audit seat type from micro_bachelors program type.
"""
from django.db import migrations


def update_program_type(apps, schema_editor):  # pylint: disable=unused-argument
    ProgramType = apps.get_model('course_metadata', 'ProgramType')
    SeatType = apps.get_model('course_metadata', 'SeatType')

    micro_bachelors = ProgramType.objects.get(name='MicroBachelors')
    verified_seat_type = SeatType.objects.get(slug='verified')

    # Clear all applicable seat types for 'MicroBachelors' and add 'verified' seat type
    micro_bachelors.applicable_seat_types.clear()
    micro_bachelors.applicable_seat_types.add(verified_seat_type)
    micro_bachelors.save()


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0335_migrateprogramslugconfiguration'),
    ]

    operations = [
        migrations.RunPython(update_program_type, migrations.RunPython.noop),
    ]
