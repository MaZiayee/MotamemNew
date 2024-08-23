from rest_framework import serializers
from website.models import Customer, Service, FAQ, Message


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id','title','image']
        
        
class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ['id','title','image','list_detail']    
        
        
class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = ['id','question','answer']    
        

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id','name','phone','email','title','message_field','created_date']  