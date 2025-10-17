from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book

def setup_groups_and_permissions():
    content_type = ContentType.objects.get_for_model(Book)

    # Createpermission
    can_view = Permission.objects.get(codename='can_view', content_type=content_type)
    can_create = Permission.objects.get(codename='can_create', content_type=content_type)
    can_edit = Permission.objects.get(codename='can_edit', content_type=content_type)
    can_delete = Permission.objects.get(codename='can_delete', content_type=content_type)

    # Creategroups
    editors_group, _ = Group.objects.get_or_create(name='Editors')
    viewers_group, _ = Group.objects.get_or_create(name='Viewers')
    admins_group, _ = Group.objects.get_or_create(name='Admins')

    #Assignpermissions
    editors_group.permissions.set([can_create, can_edit, can_view])
    viewers_group.permissions.set([can_view])
    admins_group.permissions.set([can_create, can_edit, can_delete, can_view])

    print("Groups and permissions have been set up successfully!")
