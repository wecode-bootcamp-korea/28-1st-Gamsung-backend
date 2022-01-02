import json
import bcrypt
import jwt

from django.http                import JsonResponse
from django.views               import View
from django.core.exceptions     import ValidationError

from users.models               import User
from my_settings                import SECRET_KEY, ALGORITHM
from utils.validator            import validate_email, validate_password, validate_first_name, validate_last_name, validate_dob

class SignUpView(View):
    def post(self, request):
        data          = json.loads(request.body)
        first_name    = data["first_name"]
        last_name     = data["last_name"]
        email         = data["email"]
        password      = data["password"]
        date_of_birth = data["date_of_birth"]

        try:
            if User.objects.filter(email=email).exists():
                return JsonResponse({"message": "Email is already in use"}, status=400)

            if not validate_email(email):
                return JsonResponse({"message": "Email format is invalid"}, status=400)

            if not validate_password(password):
                return JsonResponse({"message": "Password format is invalid"}, status=400)
            
            if not (validate_first_name(first_name) and validate_last_name(last_name)):
                return JsonResponse({"message": "Name format is invalid"}, status=400)

            if not validate_dob(date_of_birth):
                return JsonResponse({"message": "Date of Birth format is invalid"}, status=400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())\
                              .decode('utf-8')

            User.objects.create(
                email         = email,
                password      = hashed_password,
                first_name    = first_name,
                last_name     = last_name,
                date_of_birth = date_of_birth,
            )
            return JsonResponse({"message":"SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class SignInView(View):
    def post(self, request):
        data     = json.loads(request.body)
        email    = data["email"]
        password = data["password"].encode('utf-8')
        
        try:
            if not User.objects.filter(email=email).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=400)
            
            user_id         = User.objects.get(email=email).id
            hashed_password = User.objects.get(email=email).password.encode('utf-8')

            if not bcrypt.checkpw(password, hashed_password):
                return JsonResponse({"message": "INVALID_USER"}, status=400)
            
            access_token = jwt.encode({"id": user_id}, SECRET_KEY, algorithm=ALGORITHM)
            
            return JsonResponse({"token": access_token}, status=200)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)