# Generated by Django 3.0.5 on 2020-06-15 11:44

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_servicespage_brochure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicespage',
            name='brochure',
            field=wagtail.core.fields.StreamField([('brochure', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=30, required=True)), ('brochure_type', wagtail.core.blocks.ChoiceBlock(choices=[('pdf', 'pdf'), ('doc', 'doc'), ('docx', 'docx'), ('ppt', 'ppt'), ('pptx', 'pptx'), ('wd', 'wd')], icon='cup', max_length=3)), ('get_link', wagtail.documents.blocks.DocumentChooserBlock(blank=True, default=None, null=True))]))], blank=True, null=True),
        ),
    ]
