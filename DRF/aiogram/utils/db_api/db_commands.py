import requests



# basic = 'http://172.26.0.3:8000/'
basic = 'http://127.0.0.1:8000/'



async def get_user(user_id):
    user = requests.get(basic+'get-user', params={'user_id': f'{user_id}'}).json()
    print(user)
    if bool(user):
        pass
    else:
        user = False
    return user


async def add_rating(**kwargs):
    new_rating = requests.post(basic+'add-rating', params=kwargs).json()
    return new_rating



async def add_ratinger(**kwargs):
    new_ratinger = requests.post(basic+'add-ratinger', params=kwargs).json()
    return new_ratinger



async def get_users(direction):
    a = requests.get(basic+'get-users', params={'direction':direction}).json()
    return a

async def get_jobs(direction):
    jobs = requests.get(basic+'get-jobs',data={"direction":direction}).json()
    return jobs

async def get_user_sort_job(job):
    sort_users = requests.get(basic+'get-sort-user', data={'job':job}).json()
    print(sort_users)
    return sort_users


async def get_user_given_raitings(user_id): #user olgan raitinglarni chiqaradi
    return requests.get(basic+'get-user-given-ratings', params={'user_id':f'{user_id}'}).json()


async def get_user_img(user_id):
    user= await get_user(user_id)
    url = basic+user['user_photo']
    return url


async def add_user_db(**kwargs):
    new_user = requests.post(basic+'add-user', params=kwargs).json()
    return new_user


async def delete_user_rating(user_id, whos_rating):
    dele = requests.post(basic+'del-rating', params={'ratinger': user_id, 'whos_rating': whos_rating}).json()
    return dele


async def get_user_lang(user_id):
    print(user_id, ">"*100)
    lang = requests.get(basic+'get-user-language', params={'user_id':f'{user_id}'}).json()
    return lang


async def add_lang_to_user(user_id, lang):
    user_lang = requests.post(basic+'add-lang', data={'user_id':f'{user_id}', 'language': f'{lang}'})
    print(f'Added lang to user {user_id} lang:{lang}')
    return user_lang

async def add_phone_to_user(user_id, phone_number):
    user_phone = requests.post(basic+'add-phone', data={'user_id':f'{user_id}', 'phone_number': f'{phone_number}'})
    return user_phone

async def get_ratinger(user_id):
    print("*******************************")
    ratinger = requests.get(basic+'get-ratinger', params={'user_id':f'{user_id}'}).json()
    print(ratinger)
    print("*******************************")

    if ratinger:
        pass
    else:
        ratinger = None
    return ratinger

async def add_photo_to_user(user_id, photo_id):
    have_data = await get_user(user_id)
    print(type(have_data))
    have_data['photo_id']=f'{photo_id}'
    data = have_data
    print(data)
    ratinger = requests.post(basic+'add-photo-to-user', data=data ).json()
    return ratinger

async def get_ratinger_raitings(raitinger_id):
    raitings = requests.get(basic+'get-ratinger-raitings', data={'id':raitinger_id}).json()
    return raitings

async def get_user_raitinger_direction(user_id):
    job = requests.get(basic+'get-user-raitinger-direction', data={"user_id":user_id}).json()
    return job

async def get_all_users():
    users = requests.get(basic+'get-all-users').json()
    print(users)
    return users