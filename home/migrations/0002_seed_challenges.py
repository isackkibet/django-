from django.db import migrations

CHALLENGES = [
    {
        'title': 'Hello Django',
        'description': 'What command starts the Django development server? Submit it as the flag.',
        'flag': 'django{runserver}',
        'points': 10,
    },
    {
        'title': 'Model Basics',
        'description': 'Which file in an app defines its database models?',
        'flag': 'django{models.py}',
        'points': 10,
    },
    {
        'title': 'URL Routing',
        'description': 'Which function from django.urls connects a URL pattern to a view?',
        'flag': 'django{path}',
        'points': 20,
    },
]


def seed(apps, schema_editor):
    Challenge = apps.get_model('home', 'Challenge')
    for data in CHALLENGES:
        Challenge.objects.get_or_create(title=data['title'], defaults=data)


def unseed(apps, schema_editor):
    Challenge = apps.get_model('home', 'Challenge')
    Challenge.objects.filter(title__in=[c['title'] for c in CHALLENGES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
