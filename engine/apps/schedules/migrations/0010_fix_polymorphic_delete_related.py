# Generated by Django 3.2.18 on 2023-03-28 17:47

import common.database
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0010_team_is_sharing_resources_to_all'),
        ('slack', '0002_squashed_initial'),
        ('schedules', '0009_oncallschedulecalendar_enable_web_overrides'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oncallschedule',
            name='organization',
            field=models.ForeignKey(on_delete=common.database.NON_POLYMORPHIC_CASCADE, related_name='oncall_schedules', to='user_management.organization'),
        ),
        migrations.AlterField(
            model_name='oncallschedule',
            name='team',
            field=models.ForeignKey(default=None, null=True, on_delete=common.database.NON_POLYMORPHIC_SET_NULL, related_name='oncall_schedules', to='user_management.team'),
        ),
        migrations.AlterField(
            model_name='oncallschedule',
            name='user_group',
            field=models.ForeignKey(null=True, on_delete=common.database.NON_POLYMORPHIC_SET_NULL, related_name='oncall_schedules', to='slack.slackusergroup'),
        ),
    ]
