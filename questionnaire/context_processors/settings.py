from django.conf import settings


def load_settings(request):
    """
    A template context processor that adds the Questionnaire
     Settings to the template context.
    """
    try:
        use_session = settings.QUESTIONNAIRE_USE_SESSION
    except AttributeError:
        use_session = False

    try:
        debug_questionnaire = settings.QUESTIONNAIRE_DEBUG
    except AttributeError:
        debug_questionnaire = False

    context = {
        'debug_questionnaire': debug_questionnaire,
        'use_session': use_session
    }
    return context
