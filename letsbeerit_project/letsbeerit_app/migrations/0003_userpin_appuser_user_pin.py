# Generated by Django 4.2 on 2023-05-04 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('letsbeerit_app', '0002_alter_socialmembership_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_name', models.CharField(blank=True, max_length=30)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.AddField(
            model_name='appuser',
            name='user_pin',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='letsbeerit_app.userpin'),
        ),
    ]
