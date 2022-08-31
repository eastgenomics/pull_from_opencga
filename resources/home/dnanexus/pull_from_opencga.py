# Import ClientConfiguration and OpencgaClient class
from pyopencga.opencga_config import ClientConfiguration
from pyopencga.opencga_client import OpencgaClient
from config import USER, PASSWORD
import json
import pandas as pd

# Create an instance of OpencgaClient passing the configuration
config = ClientConfiguration(
    {"rest": {"host": "https://uat.eglh.app.zettagenomics.com/opencga/"}}
)
oc = OpencgaClient(config)
oc.login(user=USER, password=PASSWORD)

## Create main clients
users = oc.users
projects = oc.projects
studies = oc.studies
files = oc.files
jobs = oc.jobs
families = oc.families
individuals = oc.individuals
samples = oc.samples
cohorts = oc.cohorts
#panels = oc.panels
 
## Create analysis clients
#alignments = oc.alignment
#variants = oc.variant
clinical = oc.clinical
ga4gh = oc.ga4gh
 
## Create administrative clients
admin = oc.admin
meta = oc.meta
variant_operations = oc.variant_operations

result = oc.individuals.search(study='panel', limit=5, include='id')
print(result.responses)
df = pd.DataFrame.from_dict(result.responses[0]['results'])
print(df)