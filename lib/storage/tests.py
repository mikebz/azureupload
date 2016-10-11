from django.test import TestCase
from .azure_utils import AzureUtils
from django.conf import settings

# Create your tests here.
class StorageTests(TestCase):
    def test_signature(self):
        azure_utils = AzureUtils(settings.AZURE_ACCOUNT_NAME, settings.AZURE_ACCOUNT_KEY)
        result = azure_utils.generate_access_signature("foobar.dat")
        self.assertIsNotNone(result)