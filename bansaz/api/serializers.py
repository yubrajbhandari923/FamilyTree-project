from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import (
    Profile,
    Clan,
    Staffmap,
    Person,
    Relation,
    RelationCalc,
    ClanPersonRelation,
)
from rest_framework.relations import RelatedField
from django.utils.translation import gettext_lazy as _


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("country", "phone_number")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "profile",
            "first_name",
            "last_name",
        )

    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())], min_length=6
    )
    password = serializers.CharField(min_length=8)

    profile = ProfileSerializer()

    def validate_username(self, value):
        if " " in value:
            return serializers.ValidationError("username shouldnot contain <space>")
        return value

    def create(self, validated_data):
        profile_data = validated_data.pop("profile")
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        Profile.objects.create(user=user, **profile_data)
        return user


class ProfileDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "picture",
            "workplace",
            "schools",
            "colleges",
            "city",
            "relationship_status",
            "degrees",
            "education_status",
            "phone_numbers",
            "emails",
            "gender",
        ]
        # read_only_fields = "__all__"

    def update(self, instance, validated_data):
        instance.picture = validated_data.get("picture", instance.picture)
        instance.workplace = validated_data.get("workplace", instance.workplace)
        instance.schools = validated_data.get("schools", instance.schools)
        instance.colleges = validated_data.get("colleges", instance.colleges)
        instance.city = validated_data.get("city", instance.city)
        instance.relationship_status = validated_data.get(
            "relationship_status", instance.relationship_status
        )
        instance.degrees = validated_data.get("degrees", instance.degrees)
        instance.education_status = validated_data.get(
            "education_status", instance.education_status
        )
        instance.phone_numbers = validated_data.get(
            "phone_numbers", instance.phone_numbers
        )
        instance.emails = validated_data.get("emails", instance.emails)
        instance.gender = validated_data.get("gender", instance.gender)

        instance.save()
        return instance


class AccountSettingSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    get_mail_about_login = serializers.BooleanField(required=False)
    profile_viewer = serializers.CharField(required=False)
    searchable_group = serializers.CharField(required=False)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.profile.get_mail_about_login = validated_data.get(
            "get_mail_about_login", instance.profile.get_mail_about_login
        )
        instance.profile.profile_viewer = validated_data.get(
            "profile_viewer", instance.profile.profile_viewer
        )
        instance.profile.searchable_group = validated_data.get(
            "searchable_group", instance.profile.searchable_group
        )

        instance.profile.save()
        instance.save()
        return instance


class ClanORStaffMapDashboardDataSerializer(serializers.Serializer):
    tree_type = serializers.CharField()
    name = serializers.CharField()
    owner = serializers.CharField()
    date_created = serializers.DateField()
    id = serializers.IntegerField()


class UsernameRelatedField(RelatedField):
    default_error_messages = {
        "required": _("This field is required."),
        "does_not_exist": _(
            'Invalid username "{username_value}" - object does not exist.'
        ),
        "incorrect_type": _("Incorrect type. Expected pk value, received {data_type}."),
    }

    def to_internal_value(self, data):
        data = str(data)
        try:
            return self.get_queryset().get(username=data)
        except ObjectDoesNotExist:
            self.fail("does_not_exist", username_value=data)
        except (TypeError, ValueError):
            self.fail("incorrect_type", data_type=type(data).__name__)

    def to_representation(self, value):
        return str(value.username)


class ClanSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    admins = UsernameRelatedField(
        many=True, queryset=User.objects.all(), required=False
    )
    viewable_to = UsernameRelatedField(
        many=True, queryset=User.objects.all(), required=False
    )

    class Meta:
        model = Clan
        fields = "__all__"
        read_only_fields = ["id", "owner"]
        extra_kwargs = {
            "name": {"required": False},
            "description": {"required": False},
        }


class StaffMapSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    admins = UsernameRelatedField(
        many=True, queryset=User.objects.all(), required=False
    )
    viewable_to = UsernameRelatedField(
        many=True, queryset=User.objects.all(), required=False
    )

    class Meta:
        model = Staffmap
        fields = "__all__"
        read_only_fields = ["id", "owner"]
        extra_kwargs = {
            "name": {"required": False},
            "description": {"required": False},
        }


class NameRelatedField(RelatedField):
    default_error_messages = {
        "required": _("This field is required."),
        "does_not_exist": _(
            'Invalid username "{username_value}" - object does not exist.'
        ),
        "incorrect_type": _("Incorrect type. Expected pk value, received {data_type}."),
    }

    def to_internal_value(self, data):
        data = str(data)
        try:
            return self.get_queryset().get(name=data)
        except ObjectDoesNotExist:
            self.fail("does_not_exist", username_value=data)
        except (TypeError, ValueError):
            self.fail("incorrect_type", data_type=type(data).__name__)

    def to_representation(self, value):
        return str(value.name)


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
        read_only_fields = ["id"]


class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = "__all__"
        read_only_fields = ["id"]


class RelationCalculatorSerializer(serializers.ModelSerializer):
    first_relation = NameRelatedField(queryset=Relation.objects.all())
    second_relation = NameRelatedField(queryset=Relation.objects.all())
    result_relation = NameRelatedField(queryset=Relation.objects.all())

    class Meta:
        model = RelationCalc
        fields = "__all__"
        read_only_fields = ["id"]


class ClanPersonRelationSerializer(serializers.ModelSerializer):
    clan = NameRelatedField(queryset=Clan.objects.all())
    first_person = NameRelatedField(queryset=Person.objects.all())
    relation = NameRelatedField(queryset=Relation.objects.all())
    second_person = NameRelatedField(queryset=Person.objects.all())

    class Meta:
        model = ClanPersonRelation
        fields = "__all__"
        read_only_fields = ["id"]
