from django.conf.urls import url, include
from django.contrib import admin

from web import views
from wheretogo import settings
from django.conf.urls.static import static

urlpatterns = [

                  url(r'^$', views.Index, name="IndexView"),
                  url(r'^university/$', views.UniversityList, name="UniversityView"),
                  url(r'^profession/$', views.ProfessionList, name="ProfessionView"),
                  url(r'parents/$', views.ForParentslist, name='Parentslist'),
                  url(r'^tests/$', views.TestsList, name="TestsView"),
                  url(r'^calc/$', views.Calculator, name='CalculatorView'),
                  url(r'calc/result/$', views.CalcResult, name='CalcResult'),
                  url(r'university/search/$', views.UniversitySearch, name='University Search'),
                  url(r'^university/detail/(?P<id_univer>[0-9])/$', views.UniversityDetail, name="UniversityDetail"),
                  url(r'^profession/detail/(?P<id_prof>[0-9])/$', views.ProfessionDetail, name="ProfessionDetailView"),
                  url(r'^tests/detail/(?P<id_test>[0-9])/$', views.TestsDetail, name="TestsDetailView"),
                  url(r'studyprogram/detail/(?P<id_study>[0-9])/$', views.StudyProgramDetail, name="StudyprogramView"),
                  url(r'studyprogram/$', views.StudyProgramList, name='StudyProgramList')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
