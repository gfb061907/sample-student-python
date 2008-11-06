from _10gen import request, local, Forms
from models.course import Course

data = {}

data['cs'] = Course.find().limit( 100 ).sort( { 'name' : 1 } )
template = local.views.courses

action = request.get("action", None)

if "c__id" in request:
    data['c'] = Course.findOne( request.c__id )

if action == "list":
    # already setup
    pass
elif data.has_key('c') and action == "Delete":
    data['c'].remove()
    del data['c']
elif data.has_key('c') and action == "Edit":
    pass
elif action == "Save":
    data['c'] = data.get('c', Course())
    Forms.fillInObject("c_", data['c'], request)
    data['c'].save()
    del data['c']

elif action == "New":
    data['c'] = Course()

if data.has_key('c'):
    data['c']._form = Forms.Form(data['c'], "c_")
    template = local.views.course

template(data)

del request
