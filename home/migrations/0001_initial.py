# Generated by Django 3.0.5 on 2020-06-08 23:23

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('slides', wagtail.core.fields.StreamField([('home_slide', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Add additional text', max_length=100, required=True)), ('video_link', wagtail.core.blocks.URLBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Upload slide image', required=True))]))], blank=True, null=True)),
                ('video_section_subscribe', wagtail.core.fields.RichTextField(default='Input here...')),
                ('card_title', models.CharField(default='Title', max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]