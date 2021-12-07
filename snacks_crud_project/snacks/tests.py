from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack

# Create your tests here.
class TheTestsOfSnacks(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="malakkhasawneh", email="malakkhasawneh2@gmail.com", password="drmalak19966"
        )

        self.thing = Snack.objects.create(
            title="falafel", description='falafel rap', purchaser=self.user,
        )

        self.thing1 = Snack.objects.create(
            title="shawrma", description='it is so good', purchaser=self.user,
        )


    def test_string_representation(self):
        self.assertEqual(str(self.thing), "falafel")

    def test_thing_content(self):
        self.assertEqual(f"{self.thing.title}", "falafel")
        self.assertEqual(f"{self.thing.purchaser}", "malakkhasawneh")
        self.assertEqual(self.thing.description, 'falafel rap')

    def test_thing_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "falafel")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_thing_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "purchaser: malakkhasawneh")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_thing1_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="2"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "shawrma")
        self.assertTemplateUsed(response, "snack_detail.html")   

    def test_thing_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "title": "hotdog",
                "description": "very good",
                "purchaser": self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse("snack_detail", args="3"))
        self.assertContains(response, "very good")

    def test_thing_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"title": "Updated title","description":"falafel with salat","purchaser":self.user.id}
        )

        self.assertRedirects(response, reverse("snack_detail", args="1"))

    def test_thing_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="2"))
        self.assertEqual(response.status_code, 200)