from app.services.timeline_service import TimelineService
from config.app_di import AppDI


def configure_di() -> AppDI:
    di = AppDI()
    di.register_service("timeline_service", TimelineService())
    return di