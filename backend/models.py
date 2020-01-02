
from __future__ import unicode_literals
from django.db import models
# Create your models here.
# -*- coding: utf-8 -*-



# Create your models here.

# 学生信息表
class Students(models.Model):
    stu_num = models.CharField(max_length=64,primary_key=True)
    stu_name = models.CharField(max_length=64)
    stu_college = models.CharField(max_length=64)
    stu_class = models.CharField(max_length=64)
    def __unicode__(self):
        return self.student_num

# 学生活动表
class Activity(models.Model):
    stu_num = models.CharField(max_length=64,primary_key=True)
    term = models.CharField(max_length=64)
    activity_name = models.CharField(max_length=64)
    activity_num = models.SmallIntegerField()
    ischeck = models.BooleanField(default=False)
    isagree = models.BooleanField(default=False)
    def __unicode__(self):
        return self.student_num

# 专业成绩表
class Major_Grade(models.Model):
    stu_num = models.CharField(max_length=64,primary_key=True)
    term = models.CharField(max_length=64)
    stu_major_grade = models.DecimalField(max_digits=4,decimal_places=2)
    def __unicode__(self):
        return self.student_num

# 学生综合成绩表

class Comprehensive_Grade(models.Model):
    stu_num = models.CharField(max_length=64,primary_key=True)
    stu_major_grade = models.DecimalField(max_digits=3,decimal_places=1)
    activity_grade = models.DecimalField(max_digits=3,decimal_places=1)
    stu_sum_grade = models.DecimalField(max_digits=3,decimal_places=1)
    stu_rank = models.SmallIntegerField()
    def __unicode__(self):
        return self.student_num

# 奖学金申请表
class Scholar_Apply(models.Model):
    stu_num = models.CharField(max_length=64,primary_key=True)
    stu_rank = models.SmallIntegerField()
    scholar_name = models.CharField(max_length=64)
    ischeck = models.BooleanField(default=False)
    isagree = models.BooleanField(default=False)
    def __unicode__(self):
        return self.student_num

# 班级互评表
class Class_Evaluate(models.Model):
    evaluate_stu_num = models.CharField(max_length=64)
    be_evaluate_stu_num = models.CharField(max_length=64,null=True)
    grade = models.CharField(max_length=64,null=True)
    def __unicode__(self):
        return self.evaluate_stu_num

#评价数量统计
class Evaluate_Number(models.Model):
    stu_num = models.CharField(max_length=64,primary_key=True)
    A_num = models.SmallIntegerField()
    B_num = models.SmallIntegerField()
    C_num = models.SmallIntegerField()
    D_num = models.SmallIntegerField()
    evaluate_grade = models.DecimalField(max_digits=3,decimal_places=1)
    def __unicode__(self):
        return self.student_num
#是否评价
class Is_Evaluate(models.Model):
    stu_num = models.CharField(max_length=64)
    be_evaluate_num = models.CharField(max_length=64)
    be_evaluate_name = models.CharField(max_length=64)
    isevaluate = models.BooleanField(default=False)
    def __unicode__(self):
        return self.stu_num
