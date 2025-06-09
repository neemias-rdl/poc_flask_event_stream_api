from app.controllers.pages_controller import create_page_blueprint
from config.helpers import configure_di
from flask import Flask
from app.controllers.timeline_controller import create_timeline_blueprint


def create_app():   
    app = Flask(__name__)

    di = configure_di()

    timeline_bp = create_timeline_blueprint(di)
    app.register_blueprint(timeline_bp, url_prefix="/timeline")
    # Commented blueprint of the page template, used in previous debbuging attempts
    # app.register_blueprint(create_page_blueprint(di), url_prefix="/")
    return app

def main():
    app = create_app()
    app.run(debug=True, threaded=True)

if __name__ == "__main__":
    main()