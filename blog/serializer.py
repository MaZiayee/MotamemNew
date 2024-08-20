from rest_framework import serializers
from blog.models import Post,Category
#class PostSerializer(serializers.Serializer):
#    title = serializers.CharField(max_length=255)
#    id = serializers.IntegerField()

class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)  # Fetches the category name

    class Meta:
        model = Post
        fields = ['id','author','title','content','category','category_name','created_date','published_date','updated_date','status','image']