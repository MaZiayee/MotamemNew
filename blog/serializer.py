from rest_framework import serializers
from blog.models import Post,Category,Tag
#class PostSerializer(serializers.Serializer):
#    title = serializers.CharField(max_length=255)
#    id = serializers.IntegerField()

class PostSerializer(serializers.ModelSerializer):
    category_names = serializers.SerializerMethodField()  # Custom method field to get category names
    tag_names = serializers.SerializerMethodField()       # Custom method field to get tag names
    content_preview = serializers.SerializerMethodField()  # Custom field for 300 characters


    class Meta:
        model = Post
        fields = ['id','author','title','content_preview','content','category_names','tag_names','created_date','published_date','updated_date','status','image']
        
    
    def get_category_names(self, obj):
        return [category.name for category in obj.categories.all()]
    def get_tag_names(self, obj):
        return [tag.name for tag in obj.tags.all()]
    def get_content_preview(self, obj):
        return obj.content[:300]  # Return the first 300 characters of the content