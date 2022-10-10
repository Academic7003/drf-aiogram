from django.contrib import admin
from comments.models import *


admin.site.register(UserModel)
admin.site.register(RatingModel)
admin.site.register(RatingerModel)
admin.site.register(JobModel)
admin.site.register(DirectionModel)