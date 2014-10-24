import os
import hbml

import drape


class HelperWrapper:
    def __init__(self, request):
        self.__request = request

    def include_style(self, path):
        return hbml.compile(
            '%link(href=path, rel="stylesheet", type="text/css")/',
            dict(
                path=os.path.join(
                    '/',
                    self.__request.root_path(),
                    'data/compiled/css',
                    path + '.css'
                )
            )
        )

    def helpers(self):
        return [
            (attr_name, getattr(self, attr_name))
            for attr_name in dir(self)
            if attr_name[0] != '_' and attr_name != 'helpers'
        ]


def default_frame(func):
    prefix = 'app.controller.'
    assert prefix == func.__module__[:len(prefix)]

    template_path = '%s/%s.hbml' % (
        func.__module__[len(prefix):],
        func.__name__
    )

    def controller_func(request):
        var_dict = func(request)

        helper = HelperWrapper(request)
        var_dict.update(helper.helpers())

        return drape.response.Response(
            hbml.compile_file(
                os.path.normpath(
                    os.path.join(
                        request.app.root_dir,
                        'frontend/templates',
                        template_path
                    )
                ),
                var_dict
            )
        )

    return controller_func
