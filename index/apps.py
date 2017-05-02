from django.apps import AppConfig

class IndexConfig(AppConfig):
    name = 'index'

    def ready(self):
        from . import signals
        return super(IndexConfig, self).ready()