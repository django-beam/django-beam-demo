# Generated by Django 2.0.5 on 2018-05-26 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("cars", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="brand",
            name="logo",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="car",
            name="fuel",
            field=models.CharField(
                choices=[("electric", "Electric"), ("diesel", "Diesel")],
                default="electric",
                max_length=120,
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="doors",
            field=models.PositiveIntegerField(blank=True, default=2),
        ),
    ]
