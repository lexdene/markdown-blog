if __name__ == '__main__':
    import sys

    port = 8000
    if len(sys.argv) >= 2:
        port = int(sys.argv[1])

    from werkzeug.serving import run_simple
    from wsgi_index import application
    run_simple(
        'localhost',
        port,
        application,
        use_reloader=True,
        use_debugger=True
    )
