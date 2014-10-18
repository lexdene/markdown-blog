import os
app_root = os.path.dirname(__file__)

import drape.application

import app

application = drape.application.WsgiApplication(
    root_dir=app_root
)
