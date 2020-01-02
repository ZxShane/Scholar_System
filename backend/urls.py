from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'add_student$', add_student, ),
    url(r'show_all_student',show_all_student,),
    url(r'show_students', show_students, ),
    url(r'show_one_student',show_one_student,),
    url(r'add_activity',add_activity,),
    url(r'show_unchecked_activity', show_unchecked_activity, ),
    url(r'check_activity',check_activity,),
    url(r'add_scholar_apply',add_scholar_apply,),
    url(r'add_major_grade',add_major_grade,),
    url(r'check_scholar',check_scholar,),
    url(r'show_unchecked_scholar', show_unchecked_scholar, ),
    url(r'show_all_scholar',show_all_scholar,),
    url(r'calculate',calculate,),
    url(r'query_evaluate', query_evaluate, ),
    url(r'add_is_evaluate',add_is_evaluate,),
    url(r'change_is_evaluate',change_is_evaluate,),
    url(r'add_evaluate_number', add_evaluate_number, ),
    url(r'evaluate', evaluate, ),
]