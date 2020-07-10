# Generated by Django 3.0.8 on 2020-07-10 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('createDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('createDate', models.DateTimeField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.Question')),
            ],
        ),
    ]


# makemigrations 명령어는 모델을 생성하거나 모델에 변화가 있을 경우에 실행해 주어야 하는 명령어이다. makemigrations을 수행하더라도 실제로 테이블이 생성되지는 않는다. * 테이블을 실제 생성하는 명령어는 migrate명령을 통해서만 가능하다. *