from django.urls import path

from StudentApp import views

urlpatterns = [
    path('',views.login_fun,name='log'),
    path('reg',views.register_fun,name='reg'),      # it will redirect to register html file and create a account
    path('home',views.home_fun,name='home') ,        # it will redirect to home .html page
    path('add_course',views.addcourse_fun,name='add_course'),   # it will redirect to add course.html page
    path('display_course',views.display_course_fun,name='display_course') ,   # it will collect the data from course table and send to displaycourse.html page
    path('update_course/<int:courseid>',views.update_course_fun,name='update_course'), # it will update course data
    path('delete_course/<int:courseid>',views.deletecourse_fun,name='delete_course'),
    path('add_student',views.addstudent_fun,name='add_student'), # it will added for addstudent html page
    path('displaystudent',views.displaystudent_fun,name='displaystudent'),  # it will entire student data
    path('updatestudent/<int:stud_id>',views.updatestudent_fun,name='updatestudent'),
    path('deletestudent/<int:stud_id>',views.deletestudent,name='deletestudent'),
    path('logout',views.logout_fun,name='logout')

]