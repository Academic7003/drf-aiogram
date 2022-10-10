from rest_framework import serializers
from comments.models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = RatingModel
        fields = '__all__'

    def create(self):
        return RatingModel.objects.create(**self.validated_data)

class RatingerSerializer(serializers.ModelSerializer):

    class Meta:
        model = RatingerModel
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobModel
        fields = '__all__'
