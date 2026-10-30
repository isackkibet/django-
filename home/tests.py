from django.test import TestCase
from django.urls import reverse

from .models import Challenge


class ChallengeTests(TestCase):
    def setUp(self):
        self.challenge = Challenge.objects.create(
            title='Test Challenge',
            description='Find the flag.',
            flag='django{test}',
            points=10,
        )

    def test_list_shows_challenges(self):
        response = self.client.get(reverse('home:challenge_list'))
        self.assertContains(response, 'Test Challenge')

    def test_wrong_flag_is_rejected(self):
        response = self.client.post(
            reverse('home:challenge_detail', args=[self.challenge.pk]),
            {'flag': 'nope'},
        )
        self.assertContains(response, 'not correct')

    def test_correct_flag_is_accepted(self):
        url = reverse('home:challenge_detail', args=[self.challenge.pk])
        response = self.client.post(url, {'flag': 'DJANGO{TEST}'}, follow=True)
        self.assertContains(response, 'Challenge solved')
        self.assertEqual(self.client.session['solved_challenges'], [self.challenge.pk])
