# Generated by Django 3.2.5 on 2023-05-18 02:39

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_customer', models.BooleanField(default=False, verbose_name='is customer')),
                ('is_translator', models.BooleanField(default=False, verbose_name='is translator')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=50)),
                ('translatorName', models.CharField(max_length=50)),
                ('customerID', models.CharField(max_length=200)),
                ('translatorID', models.CharField(max_length=200)),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('accepted', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.user')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('First_Language', models.CharField(max_length=3)),
                ('phoneNumber', models.CharField(max_length=17)),
            ],
        ),
        migrations.CreateModel(
            name='Translator',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.user')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=17)),
                ('First_Language', models.CharField(max_length=3)),
                ('Second_Language', models.CharField(max_length=3)),
                ('price', models.IntegerField(default=0)),
                ('Certification', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Translatorr',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.user')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=17)),
                ('First_Language', models.CharField(max_length=3)),
                ('Second_Language', models.CharField(max_length=3)),
                ('price', models.IntegerField(default=0)),
                ('Certification', models.CharField(max_length=4)),
                ('rate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TranslationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='translation_requests', to=settings.AUTH_USER_MODEL)),
                ('translator', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accepted_translation_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translatorName', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.appointment')),
                ('price', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.translator')),
            ],
        ),
    ]
