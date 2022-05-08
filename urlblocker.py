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
from django.core.urlresolvers import reverse
from django.http import Http404
class BlockerAdminUrl(MiddlewareMixin):
    
    def process_request(self,request):
        if request.path.startswith(reverse("admin:index")):
            user = request.user
            if user.is_authenticated:
                if not user.is_staff:
                    # in here user is login but is not staff and cant enter to admin page
                    # you can replace Http404 with another code
                    return Http404()
                return None
            else:
                return Http404()
