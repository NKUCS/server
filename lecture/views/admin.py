from utils.api import APIView, JSONResponse
from lecture.models import Lecture
from django.db import models
from course.models import Course
from lecture.serializers import LectureSerializers
from ..serializers import LectureSerializers, GetLectureSerializer



class EditLectureAPI(APIView):
    response_class = JSONResponse
    def post(self, request):
        response_object = dict()
        # get information from frontend
        try:
            lecture_id = int(request.POST.get('lecture_id'))
            name = request.POST.get('name')
            description = request.POST.get('description')
        except Exception as exception:
            return self.error(err=exception.args, msg="lecture_id:%s\n" % (request.POST.get('lecture_id')))
        try:
            # update lecture
            Lecture.objects.filter(lecture_id=lecture_id).update(name=name, description=description)
            response_object["state_code"] = 0
            return self.success(response_object)
        except Exception as exception:
            return self.error(err=exception, msg=str(exception))
