from django.shortcuts import render
from foss.models import user ,foss,tutorial_detail as t,payment
from django.db.models import Count

def index(req):
	if req.method=='GET':
		return render(req,'index.html')
	if req.method=='POST':
		dates=[]
		try:
			objs=t.objects.filter(act_sub_date__year=req.POST['year'],act_sub_date__month=req.POST['month'])
			for i in objs:
				dates.append({'cname':i.tutorial_name,'fn':i.foss.name,'expt_date':i.exp_sub_date,'act_date':i.act_sub_date})
			objs=objs.distinct().values('publisher').annotate(c=Count('publisher')).order_by('publisher')
			usr_table=[{'count':i['c'],'pub':user.objects.filter(pk=i['publisher'])[0].name} for i in objs]
			return render(req,'index.html',{'usr_table':usr_table,'dates':dates})
		except KeyError:
			return render(req,'index.html',{'err':True})
