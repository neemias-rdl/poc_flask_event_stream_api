from app.services.timeline_service import TimelineService
from config.app_di import AppDI
from flask import Blueprint, Response, stream_with_context


def create_page_blueprint(di: AppDI):
    page_blueprint = Blueprint('page', __name__)

    @page_blueprint.route('/', methods=['GET'])
    def index():
        return '''
        <!doctype html>
        <html>
        <body>
            <h1>SSE Test</h1>
            <div id="messages"></div>
            <script>
                const evtSource = new EventSource("/timeline/get_numbers");
                evtSource.onmessage = function(event) {
                    const newElement = document.createElement("div");
                    newElement.innerHTML = "Received: " + event.data;
                    document.getElementById("messages").appendChild(newElement);
                };
            </script>
        </body>
        </html>
    '''



    return page_blueprint