from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json

from .models import Students,Activity,Class_Evaluate,Scholar_Apply,Major_Grade,Comprehensive_Grade,Evaluate_Number,Is_Evaluate


# Create your views here.

#添加学生信息

@require_http_methods(["GET"])
def add_student(request):
    response = {}
    try:
        student = Students(stu_num=request.GET.get('stu_num'),stu_name = request.GET.get('stu_name'),stu_college = request.GET.get('stu_college'),stu_class = request.GET.get('stu_class'))
        student.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# 添加专业课成绩

@require_http_methods(["GET"])
def add_major_grade(request):
    response = {}
    try:
       major_grade = Major_Grade(stu_num=request.GET.get('stu_num'),term = request.GET.get('term'),stu_major_grade = request.GET.get('stu_major_grade'))
       major_grade.save()
       response['msg'] = 'success'
       response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# 显示所有学生信息

@require_http_methods(["GET"])
def show_all_student(request):
    response = {}
    try:
        students = Students.objects.filter(stu_class = request.GET.get('stu_class'))
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", students))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# 显示所有未评价的学生

@require_http_methods(["GET"])
def show_students(request):
    response = {}
    try:
        students = Is_Evaluate.objects.filter(stu_num = request.GET.get('stu_num'),isevaluate=False)
        # be_evaluate_num = be_evaluate_students.be_evaluate_stu_num
        response['list'] = json.loads(serializers.serialize("json", students))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

#显示一个学生的信息

@require_http_methods(["GET"])
def show_one_student(request):
    response={}
    try:
        student = Students.objects.filter(stu_num=request.GET.get('stu_num'))
        response['list'] = json.loads(serializers.serialize("json",student))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg']=str(e)
        response['error_num'] = 1
    return  JsonResponse(response)

# 评价一个学生

@require_http_methods(["GET"])
def evaluate(request):
    response = {}
    try:
        evaluate_result = Class_Evaluate(evaluate_stu_num = request.GET.get('evaluate_stu_num'),be_evaluate_stu_num = request.GET.get('be_evaluate_stu_num'),grade = request.GET.get('grade'))
        evaluate_result.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def query_evaluate(request):
    response = {}
    try:
        student_num = request.GET.get('stu_num')
        evaluate_results = Class_Evaluate.objects.filter(evaluate_stu_num=student_num)
        # for evaluate_result in evaluate_results:
        #     if evaluate_result
        # evaluate_person = evaluate_sum['A'] + evaluate_sum['B'] + evaluate_sum['C'] + evaluate_sum['D']
        # evaluate_grade = (evaluate_sum['A']*95 + evaluate_sum['B']*85 + evaluate_sum['C']*75 + evaluate_sum['D']*65)/evaluate_person
        # evaluate_number = Evaluate_Number(stu_num = student_num,A_num = evaluate_sum['A'],B_num = evaluate_sum['B'],C_num = evaluate_sum['C'],D_num = evaluate_sum['D'],evaluate_grade=evaluate_grade)
        # evaluate_number.save()
        response['list']=json.loads(serializers.serialize('json',evaluate_results))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 统计一个学生评价的结果

@require_http_methods(["GET"])
def add_evaluate_number(request):
    response = {}
    try:
        evaluate_number = Evaluate_Number(stu_num = request.GET.get('stu_num'),A_num = request.GET.get('A_num'),B_num = request.GET.get('B_num'),C_num = request.GET.get('C_num'),D_num = request.GET.get('D_num'),evaluate_grade=request.GET.get('evaluate_grade'))
        evaluate_number.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# 增加一个学生的评价状态
@require_http_methods(["GET"])
def add_is_evaluate(request):
    response = {}
    try:
        is_evaluate = Is_Evaluate(stu_num = request.GET.get('stu_num'),be_evaluate_num = request.GET.get('be_evaluate_num'),be_evaluate_name = request.GET.get('be_evaluate_name'),isevaluate = False)
        is_evaluate.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# 改变一个学生的评价状态
@require_http_methods(["GET"])
def change_is_evaluate(request):
    response = {}
    try:
        Is_Evaluate.objects.filter(stu_num = request.GET.get('stu_num'),be_evaluate_num = request.GET.get('be_evaluate_num')).update(isevaluate = True)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 添加活动

@require_http_methods(["GET"])
def add_activity(request):
    response = {}
    try:
        activity = Activity(stu_num = request.GET.get('stu_num'),term = request.GET.get('term'),activity_name = request.GET.get('activity_name'),activity_num = request.GET.get('activity_num'))
        activity.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# 只查看未审核的奖学金

@require_http_methods(["GET"])
def show_unchecked_activity(request):
    response = {}
    try:
        scholars = Activity.objects.filter(ischeck=False)
        response['list'] = json.loads(serializers.serialize('json',scholars))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# 审核活动

@require_http_methods(['GET'])
def check_activity(request):
    response = {}
    try:
        Activity.objects.filter(stu_num=request.GET.get('stu_num'),activity_name = request.GET.get('activity_name')).update(ischeck=True,isagree = request.GET.get('isagree'))
        response['msg']='success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return  JsonResponse(response)

# 申请奖学金

@require_http_methods(["GET"])
def add_scholar_apply(request):
    response = {}
    try:
        scholar = Scholar_Apply(stu_num = request.GET.get('stu_num'),stu_rank = request.GET.get('stu_rank'),scholar_name = request.GET.get('scholar_name'))
        scholar.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# 审核奖学金

@require_http_methods(["GET"])
def check_scholar(request):
    response = {}
    try:
        Scholar_Apply.objects.filter(stu_num=request.GET.get('stu_num'),scholar_name=request.GET.get('scholar_name')).update(ischeck=True,isagree=request.GET.get('isagree'))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# 只查看未审核的奖学金

@require_http_methods(["GET"])
def show_unchecked_scholar(request):
    response = {}
    try:
        scholars = Scholar_Apply.objects.filter(ischeck=False)
        response['list'] = json.loads(serializers.serialize('json',scholars))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 公开所有奖学金申请状态

@require_http_methods(["GET"])
def show_all_scholar(request):
    response = {}
    try:
        scholars = Scholar_Apply.objects.all()
        response['list'] = json.loads(serializers.serialize('json',scholars))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 统计所有成绩(未测试）

@require_http_methods(["GET"])
def calculate(request):
    response = {}
    try:
        class_evaluate = Class_Evaluate.objects.filter(stu_num = request.GET.get('stu_num'))
        evaluate_grade = class_evaluate.grade
        activitys = Activity.objects.filter(stu_num = request.GET.get('stu_num'),isagree = True)
        activity_grade = 0
        for activity in activitys:
            activity_grade += activity.num
        major_grade = Major_Grade.objects.filter(stu_num = request.GET.get('stu_num'))
        sum = activity_grade*0.1+evaluate_grade*0.1+major_grade.grade*0.8
        comprehensive_grade = Comprehensive_Grade(stu_num = request.GET.get('stu_num'),stu_major_grade = major_grade,activity_grade = activity_grade,stu_sum_grade = sum,rank = 0)
        comprehensive_grade.save()
        response['list'] = json.loads(serializers.serialize('json',comprehensive_grade))
        response['msg'] = "success"
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
