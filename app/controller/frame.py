import os
import hbml

import drape

def default_frame(func):
    prefix = 'app.controller.'
    assert prefix == func.__module__[:len(prefix)]

    template_path = '%s/%s.hbml' % (
        func.__module__[len(prefix):],
        func.__name__
    )

    def controller_func(request):
        def include_style(path):
            return hbml.compile(
                '%link(href=path, rel="stylesheet", type="text/css")/',
                dict(
                    path = os.path.join(
                        '/',
                        request.root_path(),
                        'data/compiled/css',
                        path + '.css'
                    )
                )
            )

        var_dict = func(request)
        var_dict.update({
            'include_style': include_style
        })
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


