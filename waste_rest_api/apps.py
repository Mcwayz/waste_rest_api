from django.apps import AppConfig

class YourAppNameConfig(AppConfig):
    name = 'waste_rest_api'

    def ready(self):
        import waste_rest_api.signals