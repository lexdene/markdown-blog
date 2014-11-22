version = '0.0.0.1'

from . import config
import drape
drape.config.register(config)

from . import routes
