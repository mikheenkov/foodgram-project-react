# Generated by Django 3.2.7 on 2021-10-01 02:40

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(help_text="User's username field.", max_length=150, null=True, verbose_name='username')),
                ('email', models.EmailField(help_text="User's email field.", max_length=254, unique=True, verbose_name='email')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_date', models.DateTimeField(auto_now_add=True, help_text='Date of subscription between two users.', verbose_name='date of subscription')),
                ('author', models.ForeignKey(help_text='Relation to the author.', on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('follower', models.ForeignKey(help_text='Relation to the follower.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='follower')),
            ],
            options={
                'verbose_name': 'user-to-user subscription',
                'verbose_name_plural': 'user-to-user subscriptions',
            },
        ),
        migrations.CreateModel(
            name='UserRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, help_text='Note on why user has decided to add a recipe.', max_length=1024, null=True, verbose_name='note')),
                ('recipe', models.ForeignKey(help_text='Recipe that is favorited by user.', on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe', verbose_name='recipe')),
                ('user', models.ForeignKey(help_text="User's favorite recipes.", on_delete=django.db.models.deletion.CASCADE, related_name='favorite_recipes', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'user recipe relation',
                'verbose_name_plural': 'user recipe relations',
            },
        ),
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipes', models.ManyToManyField(help_text="Relation to a recipe in User's shopping cart.", to='recipes.Recipe', verbose_name='recipe')),
                ('user', models.OneToOneField(help_text='Relation to owner of the shopping cart.', on_delete=django.db.models.deletion.CASCADE, related_name='shopping_cart', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': "user's shopping cart",
                'verbose_name_plural': "user's shopping carts",
            },
        ),
        migrations.AddField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(help_text="User's favorite recipes.", through='users.UserRecipe', to='recipes.Recipe', verbose_name='favorite'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='subscriptions',
            field=models.ManyToManyField(help_text="User's subscriptions to other ones.", through='users.UserSubscription', to=settings.AUTH_USER_MODEL, verbose_name='subscription'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]