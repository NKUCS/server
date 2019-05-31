from django.conf.urls import url
from user.views.admin import CreateRoleAPI, GetRoleAPI, GetRoleTeacherListAPI, GetRoleAddTeacherListAPI, RoleTeacherAPI, CreateStudentAPI
from user.views.admin import GetRoleListAPI, DeleteRoleAPI, ModifyRoleAPI

urlpatterns = [
    url(r'create_role?$', CreateRoleAPI.as_view(), name="create_role"),
    url(r'modify_role?$', ModifyRoleAPI.as_view(), name="modify_role"),
    url(r'role_detail?$', GetRoleAPI.as_view(), name="get_role"),
    url(r'role_list?$', GetRoleListAPI.as_view(), name="get_role_list"),
    url(r'role_delete?$', DeleteRoleAPI.as_view(), name="delete_role"),
    url(r'role-teacher-list/?$', GetRoleTeacherListAPI.as_view(), name="role-teacher-list"),
    url(r'role-add-teacher-list/?$', GetRoleAddTeacherListAPI.as_view(), name="role-add-teacher-list"),
    url(r'role-teacher/?$', RoleTeacherAPI.as_view(), name="role-teacher"),

    url(r'student_create/?$', CreateStudentAPI.as_view(), name="student_create"),
]
