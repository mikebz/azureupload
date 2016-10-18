from django.test import TestCase
from .azure_utils import AzureUtils
from django.conf import settings


class StorageTests(TestCase):
    def test_signature(self):
        azure_utils = AzureUtils(settings.AZURE_ACCOUNT_NAME, settings.AZURE_ACCOUNT_KEY)
        result = azure_utils.generate_access_signature("foobar.dat")
        print "sas: " + result
        self.assertIsNotNone(result)
