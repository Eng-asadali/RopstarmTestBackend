from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from .models import vehicleCategory, vehicle


class getInventoryParentCategorySeializer(ModelSerializer):
    class Meta:
        model = vehicleCategory
        fields = '__all__'

    def create(self, validated_data):
        category = vehicleCategory.objects.create(
            name=validated_data['name'],
            status=validated_data['status'],
        )
        return True

class getInventoryCategorySeializer(ModelSerializer):
    parent_category = SerializerMethodField('get_inventory_parent_category_name')
    parent_category_id = SerializerMethodField('get_inventory_parent_category_id')

    def get_inventory_parent_category_name(self, obj):
        try:
            value = vehicleCategory.objects.get(id=obj.parent_category_id)
            return value.name
        except Exception as e:
            print(e)
            return None
    def get_inventory_parent_category_id(self, obj):
        try:
            value = vehicleCategory.objects.get(id=obj.parent_category_id)
            return value.id
        except Exception as e:
            print(e)
            return None

    class Meta:
        model = vehicle
        fields = '__all__'

class InventoryCategorySeializer(ModelSerializer):
    class Meta:
        model = vehicle
        fields = '__all__'

    def create(self, validated_data):
        parent_category = vehicleCategory.objects.get(id=validated_data['parent_category'])
        category = vehicle.objects.create(
            name=validated_data['name'],
            color=validated_data['color'],
            modal=validated_data['modal'],
            makes=validated_data['makes'],
            registration=validated_data['registration'],
            parent_category=parent_category,
            status=validated_data['status'],
        )
        return True
