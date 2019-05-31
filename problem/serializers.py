from rest_framework import serializers
from submission.models import Problem,ProblemSubmission,ProblemSubmissionCase
from submission.serializers import ProblemSubmissionTimeSerializers
from .models import Case,Tag


class GetProblemSerializer(serializers.ModelSerializer):
    cases = serializers.StringRelatedField(many=True)
    class Meta:
        model = Problem
        fields = ('name', 'description', 'teacher','runtime_limit',
         'memory_limit', 'created_at','modified_at','tags','cases')
    def get_cases(self,obj):
        return obj.cases

class GetTagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')
        
class GetCasesSerializer(serializers.ModelSerializer):
    tags = GetTagsSerializer(many=True)
    class Meta:
        model = Case
        fields = ('id', 'input', 'output','tags')


