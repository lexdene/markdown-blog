from . import routes
version = '0.0.0.1'

from . import config
import drape
drape.config.config.register(config)
