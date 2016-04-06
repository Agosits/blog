from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User 
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import student,grade,course
import datetime
# Create your views here.
@csrf_protect
def login_view(request):
    nexturl=request.GET.get('next','')
    #return HttpResponse(nexturl)
    if request.method == 'POST':    
        username = request.POST.get('ID','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        #return HttpResponse(str(username)+str(password))
        if user is not None and user.is_active:
            auth.login(request,user)
            if nexturl:
                return HttpResponseRedirect(nexturl)
            else:
                return HttpResponseRedirect('/course/main')
        else:
              err="failed,id and password dont't match OR id isn't exist"
              return render_to_response('login.html',{'err':err},context_instance=RequestContext(request))
    else:
            return render_to_response('login.html',context_instance=RequestContext(request))

@login_required(login_url='/course/login')
#@csrf_protect
def main(request):
    def deal_time():
        tmp = 1 << chosen_course.time
        if tmp&visitor.timetable != 0:
            return "Time conflict!You can't have two courses at same time.Or this course you have alreay chose."
        visitor.timetable = visitor.timetable | tmp
        visitor.save()

    def get_timetable():
        table = [(['']*6) for i in range(5)]
        table[0][0] = '8:00-9:50'
        table[1][0] = '10:10-12:00'
        table[2][0] = '13:30-15:20'
        table[3][0] = '15:30-17:20'
        table[4][0] = '18:30-20:20'
        for c in cl:
            i = c.time % 5
            if i == 0: i = 5
            i -= 1
            j = c.time // 5 +1
            if j == 6: j=5
            table[i][j] = c.name+'#'+c.classroom
        return table
    def get_grade():
        return 1
        join_year = int(visitor.sid[:4])
        g = int(datetime.date.today[0:4])-join_year
        if int(datatime.date.today[5:7]) > 8 : g += 1
        return g

    visitor = request.user.student
    cl = visitor.courses.all()
    course_list = grade.objects.filter(name=get_grade())[0].courses.all()
    err=[]

    if request.method == 'POST':
        succ = []
        for key,value in request.POST.items() :
            if value == '1':
                chosen_course = course.objects.filter(name=key)[0]
                d = deal_time()
                if d != None :
                    if d not in err:
                        err.append(d)
                else:
                    visitor.courses.add(chosen_course)
                s = 'CHOOSE SUCEESS'
                if s not in succ:
                    succ.append(s)

            if value == '2':
                try:
                    delete_course = visitor.courses.filter(name=key)[0]
                except IndexError:
                    e = 'The course you submit is not exist.You can see this maybe because you refresh the webpage and the browser resend the delete request.'
                    if e not in err:
                        err.append(e)
                else:
                    visitor.courses.remove(delete_course)
                    visitor.timetable = visitor.timetable & (~(1<<delete_course.time))
                    visitor.save()
                    delete_message = 'DELETE SUCEESS'
                    if delete_message not in succ:
                        succ.append(delete_message)
        cl = visitor.courses.all()
        table = get_timetable()
        dic = {'course_list':course_list,
                'cl':cl,
                'err':err,
                'succ':succ,
                'table':table
                }

        return render_to_response('main.html',dic,
                                        context_instance=RequestContext(request))
    else:
        #request.user.sid->grade
        table =  get_timetable()
        dic = {'course_list':course_list,
                'cl':cl,
                'table':table,
                }

        return render_to_response('main.html',dic,
                                        context_instance=RequestContext(request))
#to list:1.#sid->grade #timetable