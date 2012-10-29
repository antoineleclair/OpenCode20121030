from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Broadcast,
    )

@view_config(route_name='home', renderer='home.mako')
def home(request):
    return {'broadcasts': []}    
