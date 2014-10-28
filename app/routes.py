'define routes'
from drape.router import (
    Url,
    define_routes,
    define_controller
)

from . import controller


define_controller(controller)
define_routes(
    Url.get('', 'index.index'),
    Url.get('article/(?P<path>.+)', 'index.article'),
    Url.get('about', 'index.about'),
)
