from azure.storage.blob import BlockBlobService, ContainerPermissions
from datetime import datetime, timedelta


class AzureUtils:

    def __init__(self, account_name, account_key):
        if account_name is None:
            raise ValueError("account_name should not be None")
        if account_key is None:
            raise ValueError("account_key should not be None")
        self.account_name = account_name
        self.account_key = account_key

    def generate_access_signature(self, filename):
        """
        calls the Azure Web service to generate a temporary access signature.
        """
        block_blob_service = BlockBlobService(
            account_name=self.account_name,
            account_key=self.account_key
        )

        expire_at = datetime.utcnow()
        expire_at = expire_at + timedelta(seconds=30)

        permissions = ContainerPermissions.READ | ContainerPermissions.WRITE | ContainerPermissions.DELETE | ContainerPermissions.LIST

        sas_token = block_blob_service.generate_container_shared_access_signature(
                "tmp",
                permission=permissions,
                expiry=expire_at
        )

        return sas_token
