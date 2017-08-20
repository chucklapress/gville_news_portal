from rest_framework import serializers


from app.models import HeadlineArticle


class RSSfeedSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.CharField(allow_blank=True, required=False)
    class Meta:
        model = HeadlineArticle
        fields = ['top_stories_today','user']
        def validate_user(self, value):

            if value and len(value) > 0:
                raise serializers.ValidationError('Error')
                return value

    def create(self, validated_data):
        if "user" in validated_data:
            del validated_data["user"]
        return HeadlineArticle.objects.create(**validated_data)
