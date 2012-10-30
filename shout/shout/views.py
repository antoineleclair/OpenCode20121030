from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPBadRequest
from pyramid.url import route_url

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Broadcast,
    )

@view_config(route_name='home', renderer='home.mako', request_method='GET')
def home(request):    
    broadcasts = DBSession.query(Broadcast).all()
    return {'broadcasts': broadcasts}

@view_config(route_name='shout', request_method='POST')
def shout(request):
    broadcast = Broadcast(request.params.get('content', ''))
    DBSession.add(broadcast)
    return HTTPFound(route_url('home', request))
