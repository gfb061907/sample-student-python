from models.student import Student
from models.course import Course
from _10gen import request, local, Forms, response

data = {}

if request.action == "list":
    data['ss'] = Student.find().limit(50).sort({'name': 1})

    local.views.students(data)
else:
    myStudent = Student.findOne(request.s__id, True)

    if request.action == "Delete":
        myStudent.remove()
        response.sendRedirectTemporary("/students")

    else:
        data['courses'] = Course.find().toArray()

        if request.action == "Save":
            Forms.fillInObject("s_", myStudent, request)

            if myStudent._new:
                myStudent._new = False

            myStudent.save()
            data['msg'] = "Saved"

        if request.action == "Add" and 'course_for' in request \
                and 'score' in request:
            course_id = request.course_for
            c = Course.findOne(course_id)
            if c == None:
                data['msg'] = "Can't find course"
            else:
                myStudent.addScore(c, request.score)
                myStudent.save()

        myStudent._form = Forms.Form(myStudent, "s_")

        data['s'] = myStudent

        local.views.student( data )
