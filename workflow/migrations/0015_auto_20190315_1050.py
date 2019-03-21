# Generated by Django 2.0.7 on 2019-03-15 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0014_create_coreusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalworkflowlevel2',
            name='_created_by',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='workflow.CoreUser'),
        ),
        migrations.AddField(
            model_name='workflowlevel2',
            name='_created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workflowlevel2', to='workflow.CoreUser'),
        ),
        migrations.AlterField(
            model_name='workflowlevel2',
            name='workflowlevel1',
            field=models.ForeignKey(help_text='Primary or parent Workflow', on_delete=django.db.models.deletion.CASCADE, related_name='workflowlevel2', to='workflow.WorkflowLevel1', verbose_name='Workflow Level 1'),
        ),
    ]