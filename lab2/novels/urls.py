
from django.urls import path

from novels.views import novelsHome, readsHome, returnlist, getnovels , shownovels, deletenovels

urlpatterns = [

    path('novelshomepage', novelsHome, name='novelshome'),
    path('reads/<readname>', readsHome, name='reads'),
    path('listR',returnlist,name='list'),
    path('getnovels', getnovels ,name='novels'),
    path('getnovels/show/<int:id>',shownovels, name='shownovels'),
    path('getnovels/delete/<id>',deletenovels, name='delnovels')
]
