from django.apps import AppConfig

class CheckoutConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField' # Not in the original CI code
    name = 'checkout'

    def ready(self):
        import checkout.signals