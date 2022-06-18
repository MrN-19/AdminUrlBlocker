"""
This is a Middleware for blocking admin url for every user and it open for custom user that are staff or admin
"""
"""
for using this code copy this file in to one of you applications in django and you should introduce this middle ware in middleware list in the settings.py file
for introducing you should do like this :

    'appname.middlewarefile.className'
"""

"""Hope to enjoy"""

"""
    if you want i will be happy that you add more features in this project , Thank you
"""
from django.utils.deprecation import MiddlewareMixin
from django.http import Http404

class AdminPanelBlock(MiddlewareMixin):
    def process_request(self,request):
        """
            this function calling before calling view \n
        """
        self.check_user_access()

    def check_user_access(self,request):
        """

            this function checks path if it starts with /admin , it means a user wants to access in admin panel \n

            if user be admin or staff it doesnt have problem but else we dont allow him/her to access

        """
        if request.path.startswith("/admin"):
            user = request.user
            if user.is_authenticated:
                if not user.is_staff:
                    raise Http404()
                return None
            raise Http404()
        return None

