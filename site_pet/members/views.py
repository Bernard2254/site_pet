from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect, reverse
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.models import User, Group
from .forms import *
from django.contrib.auth.decorators import login_required


def index(request):
    roles = []
    pet_id = request.GET.get('pet', '')
    if pet_id:
        pet = get_object_or_404(Pet, id=pet_id)
    for role in MemberRole.objects.order_by('name').all():
        if pet_id:
            members = role.members.filter(pet=pet).order_by('name').all()
        else:
            members = role.members.order_by('name').all()
        roles.append({'role': role.name_plural, 'members': members})
    context = {'roles': roles, 'name' : 'members.index'}
    return render(request, 'members/index.html', context)


@login_required
def add_member(request):
    if request.method == 'POST':
        form = NewMemberForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            user = User.objects.create_user(username, email, password)
            user.groups.add(Group.objects.get(name='members'))
            member = Member()
            member.name = name
            member.email = email
            member.user = user
            member.role = MemberRole.objects.get(name='Bolsista')
            member.pet = Member.objects.filter(user=request.user)[0].pet
            member.save()
            return redirect(reverse('staff.index'))
        context = {'name': 'members.add_member', 'form': form}
        return render(request, 'members/form.html', context, status=400)
    else:
        form = NewMemberForm()
        context = {'name': 'members.add_member', 'form': form}
        return render(request, 'members/form.html', context)


@login_required
def add_tutor(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            user = User.objects.create_user(username, email, password)
            user.groups.add(Group.objects.get(name='tutors'))
            user.save()
            tutor = Member()
            tutor.name = name
            tutor.email = email
            tutor.user = user
            tutor.role = MemberRole.objects.get(name='Tutor')
            tutor.pet = Pet.objects.get(id=form.cleaned_data['pet'])
            tutor.save()
            return redirect(reverse('staff.index'))
        context = {'name': 'members.add_tutor', 'form': form}
        return render(request, 'members/tutor_form.html', context, status=400)
    else:
        form = TutorForm()
        context = {'name': 'members.add_tutor', 'form': form}
        return render(request, 'members/tutor_form.html', context)


@login_required
def all_tutors(request):
    tutors = []
    for user in Group.objects.get(name='tutors').user_set.all():
        member = Member.objects.filter(user=user)[0]
        tutors.append((member.id, member.name, member.pet.__str__()))
    json = {'data': tutors}
    return JsonResponse(json, safe=False)


@login_required
def all_members(request):
    member = Member.objects.filter(user=request.user)[0]
    json = {'data': [(m.id, m.name, m.email, m.role.name) for m in member.pet.members.all()]}
    return JsonResponse(json, safe=False)

