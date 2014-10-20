import os
app_root = os.path.dirname(__file__)

import sys
sys.path.append(app_root)
sys.path.append(
    os.path.normpath(
        os.path.join(
            app_root,
            '../../../python/site-packages'
        )
    )
)

import drape.application

import app

application = drape.application.WsgiApplication(
    root_dir=app_root
)
