from azureml.core.authentication import InteractiveLoginAuthentication
from azureml.core import Workspace

interactive_auth = InteractiveLoginAuthentication(tenant_id="99e1e721-7184-498e-8aff-b2ad4e53c1c2")
ws = Workspace.get(name='mlw-esp-udea-mar',
            subscription_id='98c08260-2de7-4d93-9e63-33e5ad008a54',
            resource_group='rg-ml-udea',
            location='eastus',
            auth=interactive_auth
            )

ws.write_config(path='.azureml')