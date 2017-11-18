# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from web.models import University, Profession,CategoryProfession, StudyProgram


class UniversityAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    model = Profession
    extra = 20

admin.site.register(StudyProgram)
admin.site.register(University, UniversityAdmin)
admin.site.register(CategoryProfession, CategoryAdmin)

admin.site.register(Profession)

# Register your models here.
