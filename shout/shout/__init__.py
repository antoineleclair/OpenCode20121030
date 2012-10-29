from pyramid.config import Configurator

from .models import (
    DBSession,
    Base,
    )

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    if settings.get('appfog') == 'true':
        engine = appfog_engine(settings)
    else:
        from sqlalchemy import engine_from_config
        engine = engine_from_config(settings, 'sqlalchemy.')
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()


def appfog_engine(settings):
    from sqlalchemy import create_engine
    import os, json
    all_config = json.loads(os.getenv("VCAP_SERVICES"))
    config = all_config['postgresql-9.1'][0]['credentials']
    connection_string = ('postgresql+psycopg2://%(username)s:%(password)s'
                        '@%(host)s:%(port)d/%(name)s')
    engine = create_engine(connection_string % config)
    return engine
