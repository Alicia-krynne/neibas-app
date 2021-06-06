from django.test import TestCase
from .models import Hood,Profile,Post,Business
from django.contrib.auth.models import User

# Create your tests here.

class HoodTestClass(TestCase):

    def setUp(self):
        self.Neiba= Hood(name = 'Alicia', location='Roysa')

    def test_instance(self):
        self.assertTrue(isinstance(self.Neiba,Hood))


    def test_save_method(self):
        self.Neiba.save_hood()
        hood = Hood.objects.all()
        self.assertTrue(len(hood) > 0)

    def test_data(self):
        self.assertTrue(self.Nei.name,"Kenya")


    def test_delete(self):
        hood = Hood.objects.filter(id=1)
        hood.delete()
        hoods = Hood.objects.all()
        self.assertTrue(len(hoods)==0)

    def test_get_hood_by_id(self):
        self.Neiba.save()
        hoods = Hood.objects.get(id=1)
        self.assertTrue(hoods.name,'zimma')


class ProfileTestClass(TestCase):

    def setUp(self):
        self.Pro= Profile(name = 'krynne', bio='black pink in your area')
        self.new_user=User(username='test',first_name='test1',last_name='test2',email='test@gmail.com')
        self.new_user.save()
        self.new_profile=Profile(user=self.new_user,bio='butter')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Pro,Profile))

    def test_save_method(self):
        self.Pro.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_data(self):
        self.assertTrue(self.Pro.name,"test")

    def test_delete(self):
        post = Profile.objects.filter(id=1)
        post.delete()
        posts = Profile.objects.all()
        self.assertTrue(len(posts)==0)

    def test_edit_profile(self):
        self.new_profile.save()
        self.update_profile = Profile.objects.filter(bio='smooth like butter').update(bio = 'butter')
        self.updated_profile = Profile.objects.get(bio='butter')
        self.assertTrue(self.updated_profile.bio,'butter')

class PostTestClass(TestCase):

    def setUp(self):
        self.Posti= Post(post='black pink in your area')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Posti,Post))

    def test_save_method(self):
        self.Posti.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_data(self):
        self.assertTrue(self.Posti.post,"test")

    def test_delete(self):
        post = Post.objects.filter(id=1)
        post.delete()
        posts = Post.objects.all()
        self.assertTrue(len(posts)==0)

    def test_get_post_by_id(self):
        self.Posti.save()
        posts = Post.objects.get(id=1)
        self.assertTrue(posts.post,'kol')



class BusinessTestClass(TestCase):

    def setUp(self):
        self.Bus= Business(name = 'fundi', description='tailors')

    def test_instance(self):
        self.assertTrue(isinstance(self.Bus,Business))


    def test_save_method(self):
        self.Bus.save_biz()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_data(self):
        self.assertTrue(self.Bus.name,"fundi")


    def test_delete(self):
        biz = Business.objects.filter(id=1)
        biz.delete()
        bizs = Business.objects.all()
        self.assertTrue(len(bizs)==0)

    def test_get_biz_by_id(self):
        self.Bus.save()
        bizs = Business.objects.get(id=1)
        self.assertTrue(bizs.name,'zimma')