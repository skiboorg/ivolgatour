# Generated by Django 2.2.7 on 2019-11-25 20:26

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Отель')),
                ('category', models.IntegerField(default=0, verbose_name='Категория (1-5), если указано 0, то категория не отображается')),
            ],
            options={
                'verbose_name': 'Отель',
                'verbose_name_plural': 'Отели',
            },
        ),
        migrations.CreateModel(
            name='Resort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Курорт')),
            ],
            options={
                'verbose_name': 'Курорт',
                'verbose_name_plural': 'Курорты',
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Название тура')),
                ('name_lower', models.CharField(db_index=True, max_length=100, null=True)),
                ('nameSlug', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('short_description', models.TextField(verbose_name='Краткое описание для главной')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Полное описание тура')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Дата')),
                ('personCount', models.IntegerField(default=0, verbose_name='Кол-во человек')),
                ('previewImage', models.ImageField(upload_to='tour_img/', verbose_name='Изображение превью (270 x 220)')),
                ('headerImage', models.ImageField(upload_to='tour_img/', verbose_name='Изображение шапки страницы полного описания тура (1920x210)')),
                ('pageH1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тег H1')),
                ('pageTitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название страницы SEO')),
                ('pageDescription', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание страницы SEO')),
                ('pageKeywords', models.TextField(blank=True, null=True, verbose_name='Keywords SEO')),
                ('priceDollar', models.IntegerField(default=0, verbose_name='Стоимость в долларах')),
                ('discountPriceDollar', models.IntegerField(default=0, verbose_name='Стоимость со скидкой в долларах')),
                ('priceEuro', models.IntegerField(default=0, verbose_name='Стоимость в евро')),
                ('discountPriceEuro', models.IntegerField(default=0, verbose_name='Стоимость со скидкой в евро')),
                ('priceRub', models.IntegerField(default=0, verbose_name='Стоимость в рублях')),
                ('discountPriceRub', models.IntegerField(default=0, verbose_name='Стоимость со скидкой в рублях')),
                ('length', models.IntegerField(default=0, verbose_name='Продолжительность тура')),
                ('isAtIndex', models.BooleanField(default=False, verbose_name='Отображать на главной?')),
                ('isActive', models.BooleanField(default=True, verbose_name='Отображать в списке туров?')),
                ('views', models.IntegerField(default=0, verbose_name='Просмотров')),
                ('rating', models.IntegerField(default=0, verbose_name='Рейтинг от 1 до 5')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Тур',
                'verbose_name_plural': 'Туры',
            },
        ),
        migrations.CreateModel(
            name='TourFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Питание')),
            ],
            options={
                'verbose_name': 'Вариант питания',
                'verbose_name_plural': 'Варианты питания',
            },
        ),
        migrations.CreateModel(
            name='TourOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Опция')),
            ],
            options={
                'verbose_name': 'Опция',
                'verbose_name_plural': 'Опции',
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tour_img', verbose_name='Изображение')),
                ('tour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tour.Tour', verbose_name='Изображение для')),
            ],
            options={
                'verbose_name': 'Изображение для тура',
                'verbose_name_plural': 'Изображения для туров',
            },
        ),
        migrations.AddField(
            model_name='tour',
            name='excludedOptions',
            field=models.ManyToManyField(related_name='excludedOptions', to='tour.TourOption', verbose_name='Не входит в стоимость'),
        ),
        migrations.AddField(
            model_name='tour',
            name='flyFrom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flyfrom', to='tour.Town', verbose_name='Вылет из'),
        ),
        migrations.AddField(
            model_name='tour',
            name='flyTo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flyto', to='tour.Town', verbose_name='Прилет в'),
        ),
        migrations.AddField(
            model_name='tour',
            name='food',
            field=models.ManyToManyField(related_name='food', to='tour.TourOption', verbose_name='Питание'),
        ),
        migrations.AddField(
            model_name='tour',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tour.Hotel', verbose_name='Отель'),
        ),
        migrations.AddField(
            model_name='tour',
            name='includedOptions',
            field=models.ManyToManyField(related_name='includedOptions', to='tour.TourOption', verbose_name='Входит в стоимость'),
        ),
    ]
