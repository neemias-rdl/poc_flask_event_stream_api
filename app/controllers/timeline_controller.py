from app.services.timeline_service import TimelineService
from config.app_di import AppDI
from flask import Blueprint, Response, stream_with_context


def create_timeline_blueprint(di: AppDI):
    timeline_service: TimelineService = di.get_service("timeline_service")

    timeline_blueprint = Blueprint('timeline', __name__)

    @timeline_blueprint.route('/get_numbers', methods=['GET'])
    def get_numbers():
        return Response(stream_with_context(timeline_service.stream_numbers()), content_type='text/event-stream')

    return timeline_blueprint