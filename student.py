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
        
            if myStudent.has_key('_new'):
                del myStudent['_new']
        
            myStudent.save()
            data['msg'] = "Saved"
        
        #
        # TODO should check request.has_key('course_for') and request.has_key('student'),
        # but there is something weird with request.has_key right now:
        #
        # if request.action == "Add":
        #    log("REQUEST: ")
        #    log(request.keys())                    ## List includes 'course_for'
        #    log(request.has_key('course_for'))     ## But this prints false
        #
        if request.action == "Add":
            course_id = request.course_for
            c = Course.findOne(course_id)
            if c == None:
                c['msg'] = "Can't find course"
            else:
                myStudent.addScore(c, request.score)
                myStudent.save()
    
        myStudent['_form'] = Forms.Form(myStudent, "s_")
    
        data['s'] = myStudent
    
        local.views.student( data )