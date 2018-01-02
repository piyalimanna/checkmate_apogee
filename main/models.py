# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# CustomUser is the extended user model
# Create your models here.

class puzzlePc(models.Model):
	idno = models.IntegerField()
	img = models.ImageField(blank=True)

	def __str__(self):
		return str(self.img_no)

class UserProfile(AbstractUser):
	#user = models.OneToOneField(User)
	score = models.IntegerField(default = 0)
	mines_left = models.IntegerField(default=20)#
	question_left = models.IntegerField(default=20)
	field_viewed = models.CharField(default="hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh", max_length=144)
	puzzleRetrieved = models.ManyToManyField(puzzlePc)

	# flag_used = model.IntegerField(default=0)
	def __str__(self):
		return self.teamname

class MinesGame(models.Model):#overview
	user = models.ForeignKey(User)
	
	def minefield(self):
		mines = [1*21001*100012*1001111110122100001*1001*100001111233211110001**2*11*101123232211212**212*1013*3123*21101**20*21101233210110001**20000000013*2000]
		return tuple(mines)


	def ques(self):
		quest = []
		for x in range (0,144):
			if (x/7!= 0):
				quest.append('n')
			else :
				quest.append('q')
		return tuple(quest)

	def __str__(self):
		return



class Question(models.Model):
	question_no = models.IntegerField()
	solution = models.CharField(max_length=50)
	question = models.CharField(max_length=10000,default="")
	puzzlePc = models.IntegerField(default=-1)#contains idno of puzzle pc associated or else -1

	def __str__(self):
		return str(self.question_no)
