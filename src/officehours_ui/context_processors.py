from django.conf import settings


def feedback(request):
    return {'FEEDBACK_EMAIL': getattr(settings, 'FEEDBACK_EMAIL', None)}


def login_url(request):
    return {'LOGIN_URL': getattr(settings, 'LOGIN_URL', None)}


def debug(request):
    return {'DEBUG': settings.DEBUG}


def spa_globals(request):
    user_data = {
        'id': request.user.id,
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
    } if request.user.is_authenticated else None
    return {
        'spa_globals': {
            'user': user_data,
            'feedback_email': getattr(settings, 'FEEDBACK_EMAIL', None),
            'debug': settings.DEBUG,
            'ga_tracking_id': settings.GA_TRACKING_ID,
            'login_url': settings.LOGIN_URL,
            'backends': {
                k: v.friendly_name
                for k, v in settings.BACKENDS.items()
            },
            'default_backend': settings.DEFAULT_BACKEND,
        }
    }
