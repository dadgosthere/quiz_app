# Generated by Django 5.0.2 on 2024-04-10 21:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='question_images/')),
                ('correct_answer', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('difficulty', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('hard', 'Hard')], max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.category')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.exam')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.topic')),
            ],
        ),
    ]
