from .test_utils import factories
from rest_framework.test import APITestCase
from ..models import AppUser, SocialGroup
from faker import Faker


class TestGroup(APITestCase):
    def setUp(self):
        self.users = factories.AppUserFactory.create_batch(10)
        self.groups = factories.SoliacGroupFactory.create_batch(2)

    def test_user_can_add_groups(self):
        for i, user in enumerate(self.users):
            if i % 2:
                AppUser.objects.filter(id=user.id).update(group_id=self.groups[0].id)
            else:
                AppUser.objects.filter(id=user.id).update(group_id=self.groups[1].id)
        
        users_updated = AppUser.objects.all()
        self.assertListEqual([user_with_group for user_with_group in users_updated if user_with_group.group_id != None],
                             self.users)