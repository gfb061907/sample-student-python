import _10gen
from _10gen import core
core.content.forms()

core.core.routes()

routes = _10gen.Routes()

routes.student = "student"
routes.add( "students" , "student" , { "extra" : { "action" : "list" } } )

routes.add( "courses" , "course" , { "extra": { "action" : "list" } } )

_10gen.routes = routes
