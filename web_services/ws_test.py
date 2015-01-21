# -*- coding: utf-8 -*-
import functools
import xmlrpclib
HOST = 'localhost'
PORT = 8069
DB = 'odoo_curso'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print "Logged in as %s (uid:%d)" % (USER,uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)


# 2. Read the sessions
model='openacademy.session'
method_name='search_read'
domain={}
sessions = call(model,method_name,domain, ['name' , 'seats' , 'taken_seats'])
#print "Sessions : ",sessions
for session in sessions:
    print "Session %s (%s seats), Taken Seats %d " % (session['name'], session['seats'],session['taken_seats'])



method_search = 'search'
domain = [('name','=','Curso odoo vip')]
course_ids = call('openacademy.course' , method_search , domain)
print "course_ids : ", course_ids
course_id = course_ids[0]




method_create='create'
# 3.create a new session
new_session_id = call(model, method_create, {
    'name' : 'Session ws',
    'course_id' : course_id,
})

print "new session id", new_session_id









