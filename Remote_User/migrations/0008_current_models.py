from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Remote_User', '0007_clientposts_model_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='detection_accuracy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=300)),
                ('ratio', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='detection_ratio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=300)),
                ('ratio', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='insurance_claim_frauds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RID', models.CharField(max_length=3000)),
                ('Sum_Insured', models.CharField(max_length=3000)),
                ('age', models.CharField(max_length=3000)),
                ('sex', models.CharField(max_length=3000)),
                ('weight', models.CharField(max_length=3000)),
                ('bmi', models.CharField(max_length=3000)),
                ('hereditary_diseases', models.CharField(max_length=3000)),
                ('no_of_dependents', models.CharField(max_length=3000)),
                ('smoker', models.CharField(max_length=3000)),
                ('city', models.CharField(max_length=3000)),
                ('bloodpressure', models.CharField(max_length=3000)),
                ('diabetes', models.CharField(max_length=3000)),
                ('regular_ex', models.CharField(max_length=3000)),
                ('job_title', models.CharField(max_length=3000)),
                ('claim', models.CharField(max_length=3000)),
                ('Prediction', models.CharField(max_length=3000)),
            ],
        ),
        migrations.RemoveField(
            model_name='clientposts_model',
            name='userId',
        ),
        migrations.DeleteModel(
            name='review_Model',
        ),
        migrations.AddField(
            model_name='clientregister_model',
            name='address',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientregister_model',
            name='gender',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientregister_model',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='clientregister_model',
            name='phoneno',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='ClientPosts_Model',
        ),
    ]
