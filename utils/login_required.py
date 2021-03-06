import jwt

from django.http       import JsonResponse

from my_settings       import SECRET_KEY, ALGORITHM
from users.models      import User


def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            payload      = jwt.decode(access_token, SECRET_KEY, algorithms = ALGORITHM) 
            user         = User.objects.get(id=payload['id'])
            request.user = user

            return func(self, request, *args, **kwargs)

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : 'Token is Invalid'}, status = 400)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'User does not exist'}, status = 400)

    return wrapper
