from django.test import TestCase

# some testing code.
class TestUsers(TestCase):
    def setUp(self):
        self.client = APIClient()
        
    def test_without_login(self):
        try:
            User.objects.get(email='andrei.hilote@assist.ro')
        except:
            pass
        """ Testing if can get response.data without login """
        self.client.logout()
        response = self.client.get('contacts')
        self.assertEqual(response.status_code, 404)


    def test_login(self):
        response = self.client.get('/api/users/details/')
        self.assertEqual(response.status_code, 200)


    def test_registration_phone_number_missing(self):
        request = self.factory.post(
        '/api/users/registration/phone-number/',
        {},
        format='json'
        )
        view = UserPhoneRegistration.as_view(action='phone')
        response = view(request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.reason_phrase, u'BAD REQUEST')
        self.assertEqual(response.data['details'], u'Expected phone number')

        
    def test_validation_phone_number_missing_data(self):
        request = self.factory.post(
        '/api/users/validation/phone-number/',
        {},
        format='json')
        view = UserPhoneRegistration.as_view(action='validate')
        response = view(request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.reason_phrase, u'BAD REQUEST')
        self.assertEqual(response.data['phone_number'], 'missing')
        self.assertEqual(response.data['code'], 'missing')
        self.assertEqual(response.data['id'], 'missing')

