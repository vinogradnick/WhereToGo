# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class StudyProgram(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    about = models.TextField()
    image = models.ImageField(upload_to='study_program/')
    biology = models.IntegerField(default=36)
    english = models.IntegerField(default=22)
    history = models.IntegerField(default=32)
    mathematics = models.IntegerField(default=27)
    russian = models.IntegerField(default=36)
    chemistry = models.IntegerField(default=36)
    geography = models.IntegerField(default=37)
    informatics = models.IntegerField(default=40)
    literature = models.IntegerField(default=32)
    society = models.IntegerField(default=42)
    physics = models.IntegerField(default=36)

    def __unicode__(self):
        return self.name


class CategoryProfession(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    about = models.TextField()
    prof_key = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Profession(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    about = models.TextField()
    image = models.ImageField(upload_to='profession/')
    money = models.IntegerField(default=0)
    cat_key = models.IntegerField(default=0)
    category_prof_key = models.ForeignKey(CategoryProfession, blank=True, null=True, on_delete=models.SET_NULL)
    study_program_key = models.ForeignKey(StudyProgram, blank=True, null=True, on_delete=models.SET_NULL)
    spec_1 = models.ImageField(upload_to='profession/specs/')
    spec_2 = models.ImageField(upload_to='profession/specs/')
    spec_3 = models.ImageField(upload_to='profession/specs/')

    def __unicode__(self):
        return self.name


class Tests(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    about = models.TextField()
    image = models.ImageField(upload_to='tests/')

    def __unicode__(self):
        return self.name


class Region(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name

class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    region_key = models.ForeignKey(Region, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name





class University(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    about = models.TextField()
    image = models.ImageField(upload_to='university/')
    site_url = models.URLField()
    address = models.CharField(max_length=200)
    nums = models.IntegerField(default=0)
    prof_key = models.ManyToManyField(Profession)
    study_key = models.ManyToManyField(StudyProgram)
    region_key = models.ForeignKey(Region, blank=True, null=True, on_delete=models.SET_NULL)
    price = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name
