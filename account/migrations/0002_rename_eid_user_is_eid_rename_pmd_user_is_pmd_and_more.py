# Generated by Django 5.1.3 on 2024-12-25 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='EID',
            new_name='is_eid',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='PMD',
            new_name='is_pmd',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='QA',
            new_name='is_qa',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='UTO',
            new_name='is_uto',
        ),
    ]