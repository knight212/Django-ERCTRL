# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import erm_room.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LiveViewFont',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('font_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Live View Font',
                'verbose_name_plural': 'Live View Fonts',
            },
        ),
        migrations.CreateModel(
            name='MicBiquadFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Mic Biquad Filter',
                'verbose_name_plural': 'Mic Biquad Filters',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=255)),
                ('default_time_limit', models.IntegerField(blank=True, default=60, null=True)),
                ('num_clues', models.IntegerField(blank=True, null=True)),
                ('clue_label', models.CharField(max_length=255)),
                ('time_remaining_label', models.CharField(max_length=255)),
                ('communication_box_label', models.CharField(max_length=255)),
                ('initial_data_feed_text', models.CharField(max_length=255)),
                ('success_screen_header', models.CharField(max_length=255)),
                ('success_screen_footer', models.CharField(max_length=255)),
                ('failure_screen_header', models.CharField(max_length=255)),
                ('failure_screen_footer', models.CharField(max_length=255)),
                ('hide_time_remaining_on_failure', models.BooleanField(default=False)),
                ('logo', sorl.thumbnail.fields.ImageField(blank=True, max_length=250, null=True, upload_to=erm_room.models.get_upload_path)),
                ('logo_max_height', models.IntegerField(blank=True, null=True)),
                ('font_color', models.CharField(max_length=255)),
                ('background_color', models.CharField(max_length=255)),
                ('widget_header_color', models.CharField(max_length=255)),
                ('widget_body_color', models.CharField(max_length=255)),
                ('game_end_screen_font_color', models.CharField(max_length=255)),
                ('game_end_screen_background_color', models.CharField(max_length=255)),
                ('transparent_data_feed_background', models.BooleanField(default=False)),
                ('transparent_timer_background', models.BooleanField(default=False)),
                ('override_css', models.TextField(blank=True, null=True)),
                ('custom_js', models.TextField(blank=True, null=True)),
                ('custom_header_includes', models.TextField(blank=True, null=True)),
                ('hide_data_feed', models.BooleanField(default=False)),
                ('hide_timer', models.BooleanField(default=False)),
                ('data_feed_distance_from_top', models.IntegerField(blank=True, null=True)),
                ('data_feed_distance_from_left', models.IntegerField(blank=True, null=True)),
                ('timer_distance_from_top', models.IntegerField(blank=True, null=True)),
                ('timer_distance_from_left', models.IntegerField(blank=True, null=True)),
                ('overlay_image', sorl.thumbnail.fields.ImageField(blank=True, max_length=250, null=True, upload_to=erm_room.models.get_upload_path)),
                ('clue_count_off_img', sorl.thumbnail.fields.ImageField(blank=True, max_length=250, null=True, upload_to=erm_room.models.get_upload_path)),
                ('clue_count_available_img', sorl.thumbnail.fields.ImageField(blank=True, max_length=250, null=True, upload_to=erm_room.models.get_upload_path)),
                ('clue_count_used_img', sorl.thumbnail.fields.ImageField(blank=True, max_length=250, null=True, upload_to=erm_room.models.get_upload_path)),
                ('clue_count_img_width', models.IntegerField(blank=True, null=True)),
                ('background_video', models.FileField(max_length=255, upload_to=erm_room.models.get_upload_path)),
                ('loop_background_video', models.BooleanField(default=True)),
                ('start_background_video_on_timer_start', models.BooleanField(default=False)),
                ('override_default_timer', models.BooleanField(default=False)),
                ('background_image', sorl.thumbnail.fields.ImageField(blank=True, max_length=250, null=True, upload_to=erm_room.models.get_upload_path)),
                ('end_game_success_background', sorl.thumbnail.fields.ImageField(blank=True, max_length=250, null=True, upload_to=erm_room.models.get_upload_path)),
                ('end_game_failure_background', sorl.thumbnail.fields.ImageField(blank=True, max_length=250, null=True, upload_to=erm_room.models.get_upload_path)),
                ('soundtrack', models.FileField(max_length=255, upload_to=erm_room.models.get_upload_path)),
                ('loop_soundtrack', models.BooleanField(default=False)),
                ('success_audio', models.FileField(max_length=255, upload_to=erm_room.models.get_upload_path)),
                ('failed_audio', models.FileField(max_length=255, upload_to=erm_room.models.get_upload_path)),
                ('audio_alert', models.FileField(max_length=255, upload_to=erm_room.models.get_upload_path)),
                ('audio_alert_on_clue_send', models.BooleanField(default=False)),
                ('audio_alert_on_image_clue_send', models.BooleanField(default=False)),
                ('audio_alert_on_clue_count_change', models.BooleanField(default=False)),
                ('play_soundtrack_on_timer_start', models.BooleanField(default=False)),
                ('video_brief', models.FileField(max_length=255, upload_to=erm_room.models.get_upload_path)),
                ('start_timer_after_video_brief', models.BooleanField(default=False)),
                ('success_video', models.FileField(max_length=255, upload_to=erm_room.models.get_upload_path)),
                ('fail_video', models.FileField(max_length=255, upload_to=erm_room.models.get_upload_path)),
                ('success_screen_after_success_video', models.BooleanField(default=True)),
                ('fail_screen_after_fail_video', models.BooleanField(default=True)),
                ('header_font_size', models.IntegerField(blank=True, null=True)),
                ('timer_font_size', models.IntegerField(blank=True, null=True)),
                ('clue_label_font_size', models.IntegerField(blank=True, null=True)),
                ('text_clue_font_size', models.IntegerField(blank=True, null=True)),
                ('room_end_header_font_size', models.IntegerField(blank=True, null=True)),
                ('room_end_footer_font_size', models.IntegerField(blank=True, null=True)),
                ('room_end_time_font_size', models.IntegerField(blank=True, null=True)),
                ('leaderboard_image', sorl.thumbnail.fields.ImageField(blank=True, max_length=250, null=True, upload_to=erm_room.models.get_upload_path)),
                ('leaderboard_room_description', models.TextField(blank=True, null=True)),
                ('display_polling_output', models.BooleanField(default=False)),
                ('lap_timer', models.BooleanField(default=False)),
                ('enable_time_warp', models.BooleanField(default=False)),
                ('display_timer_milliseconds', models.BooleanField(default=True)),
                ('live_view_font', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_live_view_fonts', to='erm_room.LiveViewFont')),
                ('mic_biquad_filter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_mic_biquad_filters', to='erm_room.MicBiquadFilter')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_name', models.CharField(max_length=255)),
                ('theme_image', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Theme',
                'verbose_name_plural': 'Themes',
            },
        ),
        migrations.AddField(
            model_name='room',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='erm_theme', to='erm_room.Theme'),
        ),
    ]