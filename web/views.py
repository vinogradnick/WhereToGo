# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from web.models import University, Tests, Profession, CategoryProfession, StudyProgram, Region


def Index(request):
    return render_to_response('layouts/index.html')


def UniversityList(request):
    univer = University.objects.all()
    region = Region.objects.all()
    return render_to_response('university/university.html', {
        'university': univer,
        'adress': region
    })


def ProfessionList(request):
    categ = CategoryProfession.objects.all()
    prof = Profession.objects.all()
    return render_to_response('profession/profession.html', {
        'profession': prof,
        'category': categ
    })


def TestsList(request):
    tests = Tests.objects.all()
    return render_to_response('layouts/tests.html', {
        'test': tests
    })


def ProfessionDetail(request, id_prof):
    prof = Profession.objects.get(id=id_prof)
    univer = University.objects.filter(prof_key__id=id_prof)
    return render_to_response('profession/profession.detail.html', {
        'profession': prof,
        'university': univer

    })


def UniversityDetail(request, id_univer):
    univer = University.objects.get(id=id_univer)
    program = StudyProgram.objects.filter(university__id=id_univer)
    return render_to_response('university/university.detail.html', {
        'university': univer,
        'study': program
    })


def Calculator(request):
    return render_to_response("layouts/calc.html")


def CalcResult(request):
    if request.method == 'GET':
        biology_form = int(request.GET.get('biology'))
        english_form = int(request.GET.get('english'))
        history_form = int(request.GET.get('history'))
        mathematics_form = int(request.GET.get('matematic'))
        russian_form = int(request.GET.get('russian'))
        chemistry_form = int(request.GET.get('chemistry'))
        geography_form = int(request.GET.get('geografy'))
        informatics_form = int(request.GET.get('informatic'))
        literature_form = int(request.GET.get('literature'))
        society_form = int(request.GET.get('society'))
        physics_form = int(request.GET.get('physic'))
        summ = biology_form + mathematics_form + english_form + history_form + russian_form + chemistry_form + geography_form + informatics_form + literature_form + society_form + physics_form
        study = StudyProgram.objects.filter(
            Q(biology__lte=biology_form) |
            Q(english__lte=english_form) |
            Q(history__lte=history_form) |
            Q(mathematics__lte=mathematics_form) &
            Q(russian__lte=russian_form) &
            Q(chemistry__lte=chemistry_form) |
            Q(geography__lte=geography_form) |
            Q(informatics__lte=informatics_form) |
            Q(literature__lte=literature_form) |
            Q(society__lte=society_form) |
            Q(physics__lte=physics_form)
        )
        return render_to_response('layouts/calc.result.html',
                                  {'program': study, 'summary': summ, 'biology': biology_form, 'english': english_form,
                                   'history': history_form, 'matematics': mathematics_form, 'russian': russian_form,
                                   'chemistry': chemistry_form, 'geography': geography_form,
                                   'literature': literature_form, 'society': society_form, 'physics': physics_form})
    else:
        return redirect('/calc/')


def TestsDetail(request, id_test):
    return render_to_response('layouts/test.detail.html')


def StudyProgramList(request):
    return render_to_response('layouts/studyprogram.html')


def StudyProgramDetail(request, id_study):
    stprog = StudyProgram.objects.get(id=id_study)
    prof = Profession.objects.filter(study_program_key__id=id_study)
    return render_to_response('layouts/study.program.detail.html', {
        'studyprogram': stprog,
        'profession': prof
    })


def ForParentslist(request):
    return render_to_response("componetns/parents.html")


def UniversitySearch(request):
    if request.GET:
        spec = request.GET.get('spec')
        adress = request.GET.get('adress')
        univer = University.objects.filter(study_key__name=spec, region_key__name=adress)
        return render_to_response('university/university.html', {'university': univer})
    else:
        return redirect('/university/')
