import os

def update_urls(app_name, viewset_name):
    """Updates Django `urls.py` with the new app's ViewSet."""
    urls_path = os.path.join(os.getcwd(), '..', 'delphi_api', 'urls.py')
    with open(urls_path, 'a') as url_file:
        url_file.write(f"\nfrom endpoints.{app_name}.views import {viewset_name}\n")
        url_file.write(f"router.register(r'{app_name}', {viewset_name}, '{app_name}')\n")


def update_settings(app_name, camelcased_app_name):
    """Adds the generated app to `INSTALLED_APPS` in `settings.py`."""
    settings_path = os.path.join(os.getcwd(), '..', 'delphi_api', 'settings.py')
    with open(settings_path, 'a') as settings_file:
        settings_file.write(f"INSTALLED_APPS.append('endpoints.{app_name}.apps.{camelcased_app_name}Config')\n")
