# Remove these sections
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Remove Google OAuth2 settings
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your_google_oauth2_key'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your_google_oauth2_secret'

# Remove Login/Logout URLs
LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/home/'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = '/'

# Remove Social Auth Pipeline
SOCIAL_AUTH_PIPELINE = (...)

# Remove from INSTALLED_APPS
'social_django',

INSTALLED_APPS = [
    # ... your existing apps ...
] 