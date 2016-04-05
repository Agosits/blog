from django.shortcuts import render_to_response,RequestContext
from journal.models import journal,comment,tag,mid
from .forms import journal_form,comment_form,user_form
from django.http import HttpResponseRedirect,HttpResponse
import datetime
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

# Create your views here
def logout_view(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

@csrf_protect
def login_view(request):
    if request.method == 'POST':    
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            return HttpResponse('okay')
        else:
        	  err="failed"
        	  if user == None:
        	  	err="use is none"
        	#  if user.is_staff==False:
        	#	err="user is not staff"
        	  return HttpResponse(err)
    else:
    		return HttpResponse("get ganma,hack zheme haowanma?")


@csrf_protect
def index(request):
	if request.method == 'POST':
		return login_view(request)
	return render_to_response('index.html',{'journalist':journal.objects.order_by('-id')[0:9],
										   'tlist':tag.objects.all(),
										   'page':1},
										   context_instance=RequestContext(request))
def show_journal(request,page):
	page = int(page)
	max_journal_id=mid.objects.filter(id=1)[0].maxid
	if (page-1)*10>max_journal_id or page<1 :
		return HttpResponse("the post page you post is wrong")
	return render_to_response('index.html',{'journalist':journal.objects.order_by('-id')[10*(page-1):10*(page-1)+9],
										   'tlist':tag.objects.all(),
										   'page':page,})
def show_tag(request,tagname):
	t = tag.objects.filter(name=tagname)[0]
	idlist = t.journals.split(',')
	postadict = {}
	for jid in idlist:
		j = journal.objects.filter(id=jid)[0]
		postadict[j.id] = j.title
	return render_to_response('tag.html',{'postadict':postadict,
										'tag':t})
@csrf_protect
@login_required(login_url='/')
def new_journal(request):
	if request.method == 'POST':
		form = journal_form(request.POST)
		if form.is_valid():
			newj = journal(time=datetime.datetime.now()+datetime.timedelta(hours=8))
			newj.title = form.cleaned_data['title']
			newj.content = form.cleaned_data['content']
			if newj.title == "":
				newj.title = newj.time 

			newtags = form.cleaned_data['tags']
			tglist = newtags.split(';');
			max_journal_id=mid.objects.filter(id=1)[0].maxid
			for tg in tglist:
				try:
					x = tag.objects.filter(name=tg)[0]
				except IndexError:
					if tg != "":
						newtg = tag(name=tg)
						newtg.journals=str(max_journal_id+1)
						newtg.save()
				else:
					s = x.journals+","+str(max_journal_id+1)
					x.journals = s
					x.save()
			s=",".join(tglist)
			newj.tags = str(newj.tags)+","+s

			newj.save()
			if (newj.id>max_journal_id):
				m=mid.objects.filter(id=1)[0]
				m.maxid=newj.id
				m.save()
				return HttpResponseRedirect('/')
			else:
				return HttpResponse("newjid<=maxid,attention please.")
		else:
			return HttpResponse("form in not valid")
	else:
		 return render_to_response('new_journal.html',context_instance=RequestContext(request))

	
def journal_content(request,x):
	x = int(x)
	try:
		j = journal.objects.filter(id=x)[0]
	except IndexError:
		return HttpResponse('the bolgpost you find is not exist.')
	else:
		return render_to_response('blogpost.html',{'post':j})

def show_comment(request):
	if request.method == 'GET':
		form = comment_form(request.GET)
		if form.is_valid():
			cd = form.cleaned_data
			newc = comment()
			newc.author = cd['author']
			newc.email = cd['email']
			newc.content = cd['content']
			newc.save()
			return HttpResponseRedirect('/comment')
		else:
			return render_to_response('comment.html',{'commentlist':comment.objects.all()})
			
	else:
		return render_to_response('comment.html',{'commentlist':comment.objects.all()})


#-------------------------------test area -----------------
def init_maxid():
	newm = mid(maxid=0)
	newm.save()

def init_fious():
	user = User.objects.create_user(username='fious',password='')
	user.save()
	
@login_required
def test(request):
	f = open('/home/fious/Desktop/test.txt','w')
	
	f.close()
	
	return HttpResponse("login okay!")


