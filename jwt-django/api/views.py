import os

from django.http import HttpResponse
from simplejson import loads
from rest_framework.views import APIView
from rest_framework.response import Response

from TeacherAssistant.settings import STATICFILES_DIRS
from utils.response import BaseResponse
from utils.jwt_auth import create_token
from extensions.auth import JwtAuthorizationAuthentication


class HomeView(APIView):
    # 通过Authorization请求头传递token
    authentication_classes = [JwtAuthorizationAuthentication, ]

    def get(self, request):
        print(request.user)
        return Response({'status': 200, 'msg': 'success', "data": None})


class LoginView(APIView):

    def post(self, request):
        ret = BaseResponse()
        # json数据
        # data = loads(request.body)
        # username = data['username']
        # password = data['password']
        # print(username, password)
        username = request.data['username']
        password = request.data['password']
        if username == "admin" and password == "000000":
            ret.msg = "登录成功"
            ret.token = create_token({"username": "admin"})
            ret.data = {'username': username, "avatar_url": f"/static/upload/avatar/1.png"}
            return Response(ret.dict)
        ret.status = 201
        ret.msg = "用户名或密码错误"
        return Response(data=ret.dict)


class UploadView(APIView):
    def post(self, request):
        img = request.FILES.get('img')
        user_id = request.POST.get("user_id")
        if img:
            file_dir = os.path.join(STATICFILES_DIRS[0], 'upload/avatar')
            with open(f'{file_dir}/{user_id}.png', 'wb') as f:
                for chunk in img.chunks():
                    f.write(chunk)
            return Response({'status': 200, "img_path": f"/static/upload/avatar/{user_id}.png"})
