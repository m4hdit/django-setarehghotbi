# Generated by Django 4.0.5 on 2022-07-22 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_alter_blogmodel_auther'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300, verbose_name='comment content')),
                ('status', models.BooleanField(default=False, verbose_name='comment status')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='comment date created')),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='commenter')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replys', to='blog.comment', verbose_name='reply comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blogmodel', verbose_name='comment post')),
            ],
        ),
    ]