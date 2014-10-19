from django.core.urlresolvers import reverse
from django.test import TestCase


class ViewTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertIn('<h1>RelationUs</h1>', response.content)

    def test_faq_page(self):
        response = self.client.get(reverse('faq'))
        self.assertIn('<h1>faq</h1>', response.content)

    # def test_profile_page(self):
    #     password = 'passsword'
    #     user = User.objects.create_user(username='tests-user', email='tests@tests.com', password=password)
    #     portfolio = Portfolio.objects.create_user()
    #     self.client.login(username=user.username, password=password)
    #     self.create_war_game(user)
    #     self.create_war_game(user, WarGame.WIN)
    #     response = self.client.get(reverse('profile'))
    #     self.assertInHTML('<p>Your email address is {}</p>'.format(user.email), response.content)
    #     self.assertEqual(len(response.context['games']), 2)
