from fastapi import FastAPI, status, Request, Response 

from conf import settings
from core import route
from datastructures.users import UserCreate, UserLogin, UserOut
from datastructures import jobs
from datastructures import ratings

from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()





origins = [
        'http://localhost:8000'
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





@route(
    request_method=app.post,
    path='/api/login',
    status_code=status.HTTP_201_CREATED,
    payload_key = 'email_password',
    service_url = settings.USERS_SERVICE_URL,
    authentication_required=False,
    post_processing_func='post_processing.access_token_generate_handler',
    response_model = 'datastructures.users.Token',

)
async def login(email_password: UserLogin,
                request: Request, response: Response):
    pass


@route(
    request_method=app.post,
    path = '/api/users',
    status_code = status.HTTP_201_CREATED,
    payload_key='user',
    service_url=settings.USERS_SERVICE_URL,
    authentication_required=False,
    post_processing_func=None,
    # authentication_token_decoder='auth.decode_access_token',
    service_authorization_checker='auth.is_admin_user',
    service_header_generator='auth.generate_request_header',
    response_model='datastructures.users.UserOut'

)
async def create_user(user: UserCreate, request: Request, response: Response):
    pass



@route(
    request_method=app.get,
    path='/api/users/',
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.USERS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='auth.decode_access_token',
    service_authorization_checker='auth.is_admin_user',
    service_header_generator='auth.generate_request_header',
    response_model='datastructures.users.UserOut'
)

async def get_users(request: Request, response: Response):
    pass



@route(
    request_method=app.get,
    path='/api/users/{id}',
    status_code=status.HTTP_200_OK,
    payload_key='user',
    service_url=settings.USERS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='auth.decode_access_token',
    service_authorization_checker='auth.is_admin_user',
    service_header_generator='auth.generate_request_header',
    response_model='datastructures.users.UserOut'
)

async def get_single_user(id: int, request: Request, response: Response):
    pass



@route(
    request_method=app.post,
    path='/api/jobs/',
    status_code = status.HTTP_201_CREATED,
    payload_key='jobs',
    service_url=settings.JOB_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='auth.decode_access_token',
    service_authorization_checker='auth.is_default_user',
    service_header_generator='auth.generate_request_header',
    response_model='datastructures.jobs.JobCreate',
    # response_list=True
)

async def create_job(job: jobs.JobCreate, request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    path='/api/jobs',
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.JOB_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='auth.decode_access_token',
    service_authorization_checker='auth.is_default_user',
    service_header_generator='auth.generate_request_header',
    response_model='datastructures.jobs.JobBase',
    response_list=True

)

async def get_jobs(request: Request, response: Response):
    pass



@route(
    request_method=app.post,
    path='/api/ratings/job',
    status_code=status.HTTP_201_CREATED,
    payload_key='ratings',
    service_url=settings.RATINGS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='auth.decode_access_token',
    service_authorization_checker='auth.is_default_user',
    service_header_generator='auth.generate_request_handler',
    response_model='',
    response_list=False
)

async def make_rating(rating: ratings.JobRating, request: Request, response: Response):
    pass


@route(
    request_method=app.get,
    path='api/ratings/job',
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.RATINGS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='auth.decode_access_token',
    service_authorization_checker='auth.is_default_user',
    service_header_generator='auth.generate_request_handler',
    response_model='datastructures.ratings.JobRating',
    response_list=True
)

async def get_job_ratings(request: Request, response: Response):
    pass 


@route(
    request_method=app.post,
    path='api/ratings/users',
    status_code=status.HTTP_201_CREATED,
    payload_key='ratings',
    service_url=settings.RATINGS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='auth.decode_access_token',
    service_authorization_checker='auth.is_default_user',
    service_header_generator='auth.generate_request_handler',
    response_model='',
    response_list=False
)

async def user_ratings(userrating: ratings.UserRating, request: Request, response: Response):
    pass



@route(
    request_method=app.get,
    path='api/users/ratings',
    status_code=status.HTTP_200_OK,
    payload_key=None,
    service_url=settings.RATINGS_SERVICE_URL,
    authentication_required=True,
    post_processing_func=None,
    authentication_token_decoder='auth.decode_access_token',
    service_authorization_checker='auth.is_default_user',
    service_header_generator='auth/generate_request.handler',
    response_model='datastructures.ratings.UserRating',
    response_list=True
)

async def get_user_ratings(request: Request, response: Response):
    pass