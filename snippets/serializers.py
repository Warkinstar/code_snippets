from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth import get_user_model


"""Hyperlinking API"""


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight", format="html"
    )

    class Meta:
        model = Snippet
        fields = [
            "url",  # detail link from HyperlinkedModelSerializer (snippet-detail)
            "id",
            "highlight",
            "owner",
            "title",
            "code",
            "linenos",
            "language",
            "style",
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Ссылки
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name="snippet-detail", read_only=True
    )

    class Meta:
        model = get_user_model()
        # url link from HyperlinkedModelSerializer (user-detail)
        fields = ["url", "id", "username", "snippets"]


"""ModelSerializer class"""

# class UserSerializer(serializers.ModelSerializer):
#     # Просто список pk
#     snippets = serializers.PrimaryKeyRelatedField(
#         many=True, queryset=Snippet.objects.all()
#     )
#
#     class Meta:
#         model = get_user_model()
#         fields = ["id", "username", "snippets"]
#
#
# class SnippetSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source="owner.username")
#     # owner = serializers.CharField(read_only=True, source="owner.email")
#
#
#     class Meta:
#         model = Snippet
#         fields = ["id", "title", "code", "linenos", "language", "style", "owner"]

"""Serializer class"""

# class SnippetSerializer(serializers.Serializer):
#     """Serializer, which can serializing Snippet model"""
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={"base_template": "textarea.html"})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default="python")
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default="friendly")
#
#     def create(self, validate_data):
#         """Create and return a new "Snippet" instance, given the validated data"""
#         return Snippet.objects.create(**validate_data)
#
#     def update(self, instance, validated_data):
#         """Update and return an existing "Snippet" instance, given the validated data."""
#         instance.title = validated_data.get("title", instance.title)
#         instance.code = validated_data.get("code", instance.code)
#         instance.linenos = validated_data.get("linenos", instance.linenos)
#         instance.language = validated_data.get("language", instance.language)
#         instance.style = validated_data.get("style", instance.language)
#         instance.save()
#         return instance
