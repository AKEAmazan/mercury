import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from server.settings import is_pro


class VersionInfo(APIView):
    def get(self, request, format=None):
        return Response({"isPro": is_pro})


# it will be used as really simple cache
welcome_msg = None


class WelcomeMessage(APIView):
    def get(self, request, format=None):
        global welcome_msg
        welcome_file = os.environ.get("WELCOME")
        if welcome_file is not None:
            if welcome_msg is None:
                if not os.path.exists(welcome_file):
                    return Response({"msg": ""})
                with open(welcome_file, encoding="utf-8", errors="ignore") as fin:
                    welcome_msg = fin.read()
            if welcome_msg is not None:
                return Response({"msg": welcome_msg})
        return Response({"msg": ""})
