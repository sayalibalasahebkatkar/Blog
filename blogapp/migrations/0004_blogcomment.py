# Generated by Django 4.0.2 on 2022-03-23 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0003_alter_blog_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('Timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogapp.blogcomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
