# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('runid', models.CharField(help_text='The RunID (ie. year)', max_length=32, verbose_name='RunID')),
                ('answer', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sortid', models.IntegerField()),
                ('value', models.CharField(max_length=64, verbose_name='Short Value')),
                ('text_en', models.CharField(max_length=200, verbose_name='Choice Text')),
                ('tags', models.CharField(max_length=64, verbose_name='Tags', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(help_text=b'eg. <tt>1</tt>, <tt>2a</tt>, <tt>2b</tt>, <tt>3c</tt><br /> Number is also used for ordering questions.', max_length=8)),
                ('text_en', models.TextField(verbose_name='Text', blank=True)),
                ('type', models.CharField(help_text="Determines the means of answering the question. An open question gives the user a single-line textfield, multiple-choice gives the user a number of choices he/she can choose from. If a question is multiple-choice, enter the choices this user can choose from below'.", max_length=32, verbose_name='Type of question', choices=[(b'open', b'Open Answer, single line [input]'), (b'open-textfield', b'Open Answer, multi-line [textarea]'), (b'choice-yesno', b'Yes/No Choice [radio]'), (b'choice-yesnocomment', b'Yes/No Choice with optional comment [radio, input]'), (b'choice-yesnodontknow', b"Yes/No/Don't know Choice [radio]"), (b'comment', b'Comment Only'), (b'choice', b'Choice [radio]'), (b'choice-freeform', b'Choice with a freeform option [radio]'), (b'dropdown', b'Dropdown choice [select]'), (b'choice-multiple', b'Multiple-Choice, Multiple-Answers [checkbox]'), (b'choice-multiple-freeform', b'Multiple-Choice, Multiple-Answers, plus freeform [checkbox, input]'), (b'range', b'Range of numbers [select]'), (b'number', b'Number [input]'), (b'timeperiod', b'Time Period [input, select]'), (b'custom', b'Custom field'), (b'sameas', b'Same as Another Question (put sameas=question.number in checks or sameasid=question.id)')])),
                ('extra_en', models.CharField(help_text='Extra information (use  on question type)', max_length=512, null=True, verbose_name='Extra information', blank=True)),
                ('checks', models.CharField(help_text=b'Additional checks to be performed for this value (space separated)  <br /><br />For text fields, <tt>required</tt> is a valid check.<br />For yes/no choice, <tt>required</tt>, <tt>required-yes</tt>, and <tt>required-no</tt> are valid.<br /><br />If this question is required only if another question\'s answer is something specific, use <tt>requiredif="QuestionNumber,Value"</tt> or <tt>requiredif="QuestionNumber,!Value"</tt> for anything but a specific value.  You may also combine tests appearing in <tt>requiredif</tt> by joining them with the words <tt>and</tt> or <tt>or</tt>, eg. <tt>requiredif="Q1,A or Q2,B"</tt>', max_length=512, null=True, verbose_name='Additional checks', blank=True)),
                ('footer_en', models.TextField(help_text=b'Footer rendered below the question interpreted as textile', verbose_name='Footer', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('redirect_url', models.CharField(default=b'/static/complete.html', help_text=b'URL to redirect to when Questionnaire is complete. Macros: $SUBJECTID, $RUNID, $LANG', max_length=128)),
            ],
            options={
                'permissions': (('export', 'Can export questionnaire answers'), ('management', 'Management Tools')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sortid', models.IntegerField()),
                ('heading', models.CharField(max_length=64)),
                ('checks', models.CharField(help_text=b'Current options are \'femaleonly\' or \'maleonly\' and shownif="QuestionNumber,Answer" which takes the same format as <tt>requiredif</tt> for questions.', max_length=256, blank=True)),
                ('text_en', models.TextField(help_text=b"This is interpreted as Textile: <a href='http://en.wikipedia.org/wiki/Textile_%28markup_language%29' target='_blank'>http://en.wikipedia.org/wiki/Textile_(markup_language)</a>", verbose_name='Text')),
                ('questionnaire', models.ForeignKey(to='questionnaire.Questionnaire')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RunInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('random', models.CharField(max_length=32)),
                ('runid', models.CharField(max_length=32)),
                ('emailcount', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('emailsent', models.DateTimeField(null=True, blank=True)),
                ('lastemailerror', models.CharField(max_length=64, null=True, blank=True)),
                ('state', models.CharField(max_length=16, null=True, blank=True)),
                ('cookies', models.TextField(null=True, blank=True)),
                ('tags', models.TextField(help_text='Tags active on this run, separated by commas', blank=True)),
                ('skipped', models.TextField(help_text='A comma sepearted list of questions to skip', blank=True)),
                ('questionset', models.ForeignKey(blank=True, to='questionnaire.QuestionSet', null=True)),
            ],
            options={
                'verbose_name_plural': 'Run Info',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RunInfoHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('runid', models.CharField(max_length=32)),
                ('completed', models.DateField()),
                ('tags', models.TextField(help_text='Tags used on this run, separated by commas', blank=True)),
                ('skipped', models.TextField(help_text='A comma sepearted list of questions skipped by this run', blank=True)),
                ('questionnaire', models.ForeignKey(to='questionnaire.Questionnaire')),
            ],
            options={
                'verbose_name_plural': 'Run Info History',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(default=b'inactive', max_length=16, verbose_name='State', choices=[(b'active', 'Active'), (b'inactive', 'Inactive')])),
                ('surname', models.CharField(max_length=64, null=True, verbose_name='Surname', blank=True)),
                ('givenname', models.CharField(max_length=64, null=True, verbose_name='Given name', blank=True)),
                ('email', models.EmailField(max_length=75, null=True, verbose_name='Email', blank=True)),
                ('gender', models.CharField(default=b'unset', max_length=8, verbose_name='Gender', blank=True, choices=[(b'unset', 'Unset'), (b'male', 'Male'), (b'female', 'Female')])),
                ('nextrun', models.DateField(null=True, verbose_name='Next Run', blank=True)),
                ('formtype', models.CharField(default=b'email', max_length=16, verbose_name='Form Type', choices=[(b'email', 'Subject receives emails'), (b'paperform', 'Subject is sent paper form')])),
                ('language', models.CharField(default=b'en', max_length=2, verbose_name='Language', choices=[(b'en', b'English')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='runinfohistory',
            name='subject',
            field=models.ForeignKey(to='questionnaire.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='runinfo',
            name='subject',
            field=models.ForeignKey(to='questionnaire.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='questionset',
            field=models.ForeignKey(to='questionnaire.QuestionSet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='questionnaire.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(help_text='The question that this is an answer to', to='questionnaire.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='subject',
            field=models.ForeignKey(help_text='The user who supplied this answer', to='questionnaire.Subject'),
            preserve_default=True,
        ),
    ]
