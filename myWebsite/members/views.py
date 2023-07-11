from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.views.generic import View
from django.shortcuts import redirect
# Create your views here.

def members(request):
    template = loader.get_template('home.html')
    members = Member.objects.all().values
    
    context = {
        'myMembers' : members,
    }
    
    return HttpResponse(template.render(context, request))

def details(request, id):
    template = loader.get_template('details.html')
    member = Member.objects.get(id=id)
    context = {
        'member' : member,
    }
    
    return HttpResponse(template.render(context, request))

class MemberAddView(View):
    def get(self, request):
        template = loader.get_template('add.html')
        member = Member()
        context = {
        'member' : member,
        }
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        phone = request.POST.get('phone')
        joinedDate = request.POST.get('joinedDate')
        
        member = Member()
        member.firstName = firstName
        member.lastName = lastName
        member.phone = int(phone)
        member.joinedDate = joinedDate
        member.save()
        
        return redirect('/members')
    
class MemberEditView(View):
    def get(self, request, id):
        template = loader.get_template('edit.html')
        member = Member.objects.get(id=id)
        context = {
        'member' : member,
        }
        return HttpResponse(template.render(context, request))
    
    def post(self, request, id):
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        phone = request.POST.get('phone')
        joinedDate = request.POST.get('joinedDate')
        
        member = Member.objects.get(id=id)
        member.firstName = firstName
        member.lastName = lastName
        member.phone = int(phone)
        member.joinedDate = joinedDate
        member.save()
        
        return redirect('/members')
    
class MemberDeleteView(View):
    def get(self, request, id):
        template = loader.get_template('delete.html')
        member = Member.objects.get(id=id)
        context = {
        'member' : member,
        }
        return HttpResponse(template.render(context, request))
    
def deleteMember(request, id):
    member = Member.objects.get(id=id)
    
    member.delete()
    
    return redirect('/members')
