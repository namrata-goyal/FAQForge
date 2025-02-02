INSTALLED_APPS = [
    ...
    'ckeditor',
    'faqs',
]


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1', 
    }
}

# Configure Language
LANGUAGES = [
    ('en', 'English'),
    ('hi', 'Hindi'),
    ('bn', 'Bengali'),
    #  We Can Add more languages if needed
]
