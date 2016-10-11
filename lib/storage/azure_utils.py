from azure.storage.blob import BlobService, BlobSharedAccessPermissions
from azure.storage import AccessPolicy, SharedAccessPolicy
from datetime import datetime, timedelta

class AzureUtils:

    def __init__(self, account_name, account_key):
        if account_name is None: raise ValueError("account_name should not be None")
        if account_key is None: raise ValueError("account_key should not be None")
        
        self.account_name = account_name
        self.account_key = account_key

    def generate_access_signature(self, filename):
        """
        calls the Azure Web service to generate a temporary access signature.
        """
        blob_service = BlobService(
            account_name=self.account_name, 
            account_key=self.account_key
        )

        expire_at = datetime.utcnow()
        expire_at = expire_at + timedelta(seconds = 30)
        access_policy = AccessPolicy(permission=BlobSharedAccessPermissions.WRITE, expiry=expire_at.isoformat())
        
        sas_token = blob_service.generate_shared_access_signature( 
            container_name="tmp",
            blob_name = filename, 
            shared_access_policy=SharedAccessPolicy(access_policy)
        )
        return sas_token