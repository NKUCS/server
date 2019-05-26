from django.conf.urls import url
from lecture.views.admin import EditLectureAPI

urlpatterns = [
    url(r'edit-lecture/?$', EditLectureAPI.as_view(), name="edit-lecture"),

]
