from django.urls import path
from website.views import *

urlpatterns = [
   # path('', home, name = 'home'),
   # path('about/', about, name= 'about')
   path('api/Customers/', api_Customers_list, name='api_Customers_list'),
   path('api/services/', api_Services_list, name='api_Services_list'),
   path('api/message/', ApiMessage.as_view(), name='api_message_list'),
   path('api/FAQ/', api_FAQ_list, name='api_FAQ_list'),

]