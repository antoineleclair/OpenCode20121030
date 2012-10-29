from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Broadcast,
    )

@view_config(route_name='home', renderer='home.mako')
def home(request):
    if (request.method == 'POST'):
        broadcast = Broadcast(request.params.get('content', ''))
        DBSession.add(broadcast)
    broadcasts = DBSession.query(Broadcast).all()
    return {'broadcasts': broadcasts}
