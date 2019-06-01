from utils.api import APIView, JSONResponse
from lecture.models import Lecture, LectureProblem
from django.db import models
from course.models import Course
from lecture.serializers import LectureSerializers
from ..serializers import LectureSerializers, GetLectureSerializer
from problem.models import Problem
from problem.models import Case
from submission.models import ProblemSubmission, ProblemSubmissionCase


def select_lecture_bycourse(course):
    lecture_list = set()
    lectures=Lecture.objects.filter(course=course)
    for lecture in lectures:
        lecture_list.add(lecture)
    return lecture_list

def select_lecture_byname(name):
    lecture_list = set()
    lectures=Lecture.objects.filter(name=name)
    for lecture in lectures:
        lecture_list.add(lecture)
    return lecture_list


class ShowLecture(APIView):
    response_class = JSONResponse
    def get(self, request):
        response_object = dict()
        print("hello")
        # get information from frontend
        try:
            course_id = int(request.GET.get('course_id'))
        except Exception as exception:
            return self.error(err=exception.args, msg="course_id:%s\n"%(request.POST.get('course_id')))
        try:
            # return lectures to the frontend
            lecture_list=list(select_lecture_bycourse(course_id))
            for i in range(len(lecture_list)):
                response_object['key']=i
                response_object['name']=lecture_list[i].name
                response_object["source"]=lecture_list[i].description
                print("cxq")
                print(response_object)
            return self.success(response_object)
        except Exception as exception:
            return self.error(err=exception, msg=str(exception))


class ShowMyLecturesAPI(APIView):
    response_class = JSONResponse
    def get(self, request):
        # initialize the response object
        response_object = dict()
        # get information from frontend
        try:
            page = int(request.GET.get('page'))
            course_id = int(request.GET.get('course_id'))
            page_length = int(request.GET.get('page_length'))
        except Exception as exception:
            return self.error(err=exception.args, msg="course_id:%s, page:%s\n"%(request.GET.get('course_id'), request.GET.get('page')))
        try:
            # query from database
            lectures_amount = Lecture.objects.filter(course=course_id).count()
            lectures_list = Lecture.objects.filter(course=course_id)[(page - 1) * page_length : page * page_length].values('id', 'name')
            response_object['total_counts'] = lectures_amount
            response_object['lectures'] = LectureSerializers(lectures_list, many=True).data
            return self.success(response_object)
        except Exception as exception:
            return self.error(err=exception.args, msg=str(exception))


class GetLectureByNameAPI(APIView):
    response_class = JSONResponse
    def get(self, request):
        # initialize the response object
        response_object = dict()
        # get information from frontend
        try:
            page = int(request.GET.get('page'))
            course_id = int(request.GET.get('course_id'))
            page_length = int(request.GET.get('page_length'))
            name = request.GET.get('name')
        except Exception as exception:
            return self.error(err=exception.args, msg="course_id:%s, page:%s\n"%(request.GET.get('course_id'), request.GET.get('page')))
        try:
            # query from database filter the specific data
            query_set = Lecture.objects.filter( course_id=course_id, name__icontains=name)
            lectures_amount = query_set.count()
            lectures_list = query_set[(page - 1) * page_length : page * page_length].values('id', 'name')
            response_object['total_counts'] = lectures_amount
            response_object['lectures'] = LectureSerializers(lectures_list, many=True).data
            return self.success(response_object)
        except Exception as exception:
            return self.error(err=exception.args, msg=str(exception))


class PracticeSubmission(APIView):
    response_class = JSONResponse

    def get(self, request):
        response_object = dict()
        # get information from frontend
        try:
            page = int(request.GET.get("page"))
            page_length = int(request.GET.get("page_length"))
            problem_id = int(request.GET.get('problem_id'))
            student_id = int(request.GET.get("student_id"))
        except Exception as exception:
            return self.error(err=exception.args, msg="problem_id:%s, name:%s, description:%s\n"%(request.GET.get('problem_id')))
        # get data from database
        try:
            query_set = ProblemSubmission.objects.filter(problem_id=problem_id,student_id=student_id)
            submission_id = query_set[(page - 1) * page_length: page * page_length].values("id")
            submission_count = query_set.count()
            if submission_count == 0:
                response_object['total_counts'] = submission_count
                return self.success(response_object)
            query_set_case = ProblemSubmissionCase.objects.filter(problem_submission=submission_id)
            submission_list = query_set[(page - 1) * page_length: page * page_length].values("id", "created_at", "runtime", "memory", "language")
            case_list = query_set_case.values("problem_submission", "case_status", "case")
            for sub in submission_list:
                for case in case_list:
                    if sub["id"] == case["problem_submission"]:
                        sub["status"] = case["case_status"]
                        sub["case"] = case["case"]
                if "status" not in sub:
                    sub["status"] = "Accepted"
                    sub["case"] = -1
            response_object['total_counts'] = submission_count
            response_object['submission_list'] = LectureSerializers(submission_list, many=True).data
            return self.success(response_object)
        except Exception as exception:
            return self.error(err=exception.args, msg=str(exception))


class PracticeExample(APIView):
    response_class = JSONResponse

    # get information from frontend
    def get(self,request):
        response_object = dict()
        try:
            case_id = int(request.GET.get("case"))
        except Exception as exception:
            return self.error(err=exception.args, msg="problem_id:%s, name:%s, description:%s\n" % (request.GET.get('problem_id')))
        # get data from database
        try:
            case_set = Case.objects.filter(case_id=case_id)
            response_object['case'] = LectureSerializers(case_set, many=True).data
            return self.success(response_object)
        except Exception as exception:
            return self.error(err=exception.args, msg=str(exception))


class GetAllMessage(APIView):
    def get(self, request):
        results = []
        try:
            allMessage = Message.objects.all()
            result = [{
					'content': '第1次作业提交时间将要截止',
					'course_name': '数据结构',
				},{
					'content': '第2次作业提交时间将要截止',
					'course_name': '数据结构',
				},{
					'content': '第3次作业提交时间将要截止',
					'course_name': '数据结构',
				},{
					'content': '第4次作业提交时间将要截止',
					'course_name': '数据结构',
				}]
            for message in allMessage :
                content = message.content
                courseName = message.course.name
                results.append({
                    'content' : content,
                    'course_name' : courseName
                })
            return self.success(result)
        except Exception as e:
            # not found
            return self.error(msg=str(e), err=e.args)