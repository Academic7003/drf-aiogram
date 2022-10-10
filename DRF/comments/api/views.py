from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from comments.models import *
from comments.api.serializers import *

# import logging
# logger_warning = logging.getLogger('django_warning')


@api_view(['GET'])
def get_users(request):
    direction = request.GET.get('direction')

    users = UserModel.objects.filter(user_job__direction__name=direction)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_ratings(request):
    ratings = RatingModel.objects.all()
    serializer = RatingSerializer(ratings, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_rating(request):
    ratinger = int(request.GET.get('ratinger'))
    whos_rating = int(request.GET.get('whos_rating'))
    rating = int(request.GET.get('rating'))
    z = RatingModel(ratinger =ratinger, whos_rating=whos_rating, rating=rating)
    return Response({f'{z.save()}'})


@api_view(['GET'])
def get_user(request):
    user_id = request.GET.get('user_id')
    user = UserModel.objects.filter(user_id=user_id).first()
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_given_ratings(request):
    whos_rating = request.GET.get('user_id')
    ratings = RatingModel.objects.filter(whos_rating=whos_rating)
    serializer = RatingSerializer(ratings, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_rating(request):
    user_id = request.GET.get('user_id')
    whos_rating = request.GET.get('whos_rating')
    rating = RatingModel.objects.filter(ratinger=user_id, whos_rating=whos_rating).first()
    if rating:
        serializer = RatingSerializer(rating)
        return Response(serializer.data)
    return Response(False)

@api_view(["POST"])
def add_user(request):
    user_id = request.GET.get('user_id')
    full_name = request.GET.get('full_name')
    photo_id = request.GET.get('photo_id')
    z = UserModel(user_id=user_id, full_name=full_name, photo_id=photo_id)
    return Response({f'{z.save()}'})

@api_view(["POST"])
def delete_user_ratings(request):
    ratinger = request.GET.get('ratinger')
    whos_rating = request.GET.get('whos_rating')
    z = RatingModel.objects.filter(ratinger=int(ratinger), whos_rating=int(whos_rating)).first()
    z.delete()
    return Response({'result': 'True'})

@api_view(["POST"])
def add_ratinger(request):
    user_id = request.GET.get('user_id')
    language = request.GET.get('language')
    phone_number = request.GET.get('phone_number', None)
    z = RatingerModel(user_id=user_id, language=language, phone_number=phone_number)
    return Response({f'{z.save()}'})


@api_view(["POST"])
def update_user_photo_id(request):
    user_id = request.GET.get('user_id')
    photo_id = request.GET.get('photo_id')
    user = UserModel.objects.filter(user_id=user_id).first()
    serializer = UserSerializer(user, data={'photo_id': f'{photo_id}'})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def get_user_lang(request):

    user_id = int(request.GET.get('user_id'))
    user = RatingerModel.objects.get(user_id=user_id)
    print(user.language)
    # logger_warning.warning(f"{RatingerSerializer(user).data}") ==>loggin<==

    return Response(user.language)

@api_view(['POST'])
def add_lang(request):
    print(request.data['user_id'])
    user = RatingerModel.objects.get(user_id=request.data['user_id'])
    serializer = RatingerSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(False)

@api_view(['GET'])
def get_ratinger(request):
    user_id = int(request.GET.get('user_id'))
    try:
        ratinger = RatingerModel.objects.get(user_id=user_id)
    except:
        ratinger = None
    if ratinger:
        serializer = RatingerSerializer(ratinger)
        return  Response(serializer.data)
    return Response(False)

@api_view(['POST'])
def add_ratinger(request):
    user_id = int(request.GET.get('user_id'))
    z = RatingerModel(user_id=user_id)
    print(z.save())
    return Response(RatingerSerializer(z).data)


@api_view(['POST'])
def add_phone_ratinger(request):
    user = RatingerModel.objects.get(user_id=request.data['user_id'])
    serializer = RatingerSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def add_photo_to_user(request):
    user = UserModel.objects.get(user_id=request.data['user_id'])
    serializer = UserSerializer(user, data=request.data)

    if serializer.is_valid():

        serializer.save()
        return Response(serializer.data)
    print(serializer.errors)
    return Response(serializer.errors)


@api_view(['GET'])
def get_jobs(request):
    data = request.data
    direction = data['direction']
    jobs = JobModel.objects.filter(direction__name=direction)
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_sort_users_job(request):
    data = request.data
    users = UserModel.objects.filter(user_job__name=data['job'])
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_ratinger_raitings(request):
    data = request.data
    raitings = RatingModel.objects.filter(ratinger=data['id'])
    serializer = RatingSerializer(raitings, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_user_raitinger_direction(request):
    data = request.data
    direct = UserModel.objects.get(user_id=data['user_id'])
    return Response(f'{direct.user_job.direction.name}')


@api_view(["GET"])
def get_all_users(request):
    data = request.data
    direct = UserModel.objects.all()
    serializer = UserSerializer(direct, many=True)

    return Response(serializer.data)