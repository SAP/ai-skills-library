# File:    skills/aicore-sdk-python/assets/batch_service.py
# Install: uv add sap-ai-sdk-gen
# Run:     uv run assets/batch_service.py
#
# LLM Batch Service — submit, poll, list, inspect, cancel and delete batch jobs.
# Verbatim from docs-python examples batch-service.mdx (async variant omitted).
# Requires an object store secret + a pre-uploaded input.jsonl. Replace the ai:// URIs.
# Credentials: run 'aicore configure' or see aicore-admin-resources/references/SETUP.md
# See: https://help.sap.com/docs/sap-ai-core/generative-ai/quick-start

import time
from gen_ai_hub.batch_service import BatchService

batch_service = BatchService()

# Or with an explicit proxy client:
# from gen_ai_hub.proxy import get_proxy_client
# batch_service = BatchService(proxy_client=get_proxy_client('gen-ai-hub'))

INPUT_URI = "ai://<object_store_secret_name>/<path>/input.jsonl"
OUTPUT_URI = "ai://<object_store_secret_name>/<output_folder>/"
MODEL = "gpt-4.1"
PROVIDER = "azure-openai"

create_response = batch_service.create(
    type="llm-native",
    input_uri=INPUT_URI,
    output_uri=OUTPUT_URI,
    provider=PROVIDER,
    model=MODEL,
)

BATCH_ID = create_response.id
print(f"Batch ID: {BATCH_ID}")
print(f"Status:   {create_response.status}")
print(f"Message:  {create_response.message}")

# Check Batch Status
TERMINAL_STATUSES = {"COMPLETED", "FAILED", "CANCELLED"}
POLLING_INTERVAL = 30

while True:
    status_response = batch_service.get_status(BATCH_ID)
    current = status_response.current_status
    print(f"[{time.strftime('%H:%M:%S')}] Status: {current}  ->  target: {status_response.target_status}")
    if current in TERMINAL_STATUSES:
        break
    time.sleep(POLLING_INTERVAL)

print(f"Final status: {current}")
if status_response.message:
    print(f"Message: {status_response.message}")

# List all batch jobs
list_response = batch_service.list()
print(f"Total batch jobs: {list_response.count}")
for job in list_response.resources or []:
    print(f"  {job.id}  |  {job.provider}  |  {job.status}")

# Get full details
detail = batch_service.get(BATCH_ID)
print(f"ID:         {detail.id}")
print(f"Type:       {detail.type}")
print(f"Provider:   {detail.provider}")
print(f"Created at: {detail.created_at}")
print(f"Input URI:  {detail.input.uri}")
print(f"Output URI: {detail.output.uri}")
print(f"Model:      {detail.spec.get('model') if detail.spec else None}")
print(f"Status:     {detail.status.current_status}")
print(f"Updated at: {detail.status.updated_at}")
if detail.status.message:
    print(f"Message:    {detail.status.message}")

# Cancel a batch job
cancel_response = batch_service.cancel(BATCH_ID)
print(f"ID:      {cancel_response.id}")
print(f"Message: {cancel_response.message}")

while True:
    status_response = batch_service.get_status(BATCH_ID)
    print(f"Status: {status_response.current_status}")
    if status_response.current_status in TERMINAL_STATUSES:
        break
    time.sleep(10)

# Delete a batch job
status_response = batch_service.get_status(BATCH_ID)
if status_response.current_status not in {"COMPLETED", "FAILED", "CANCELLED"}:
    print(f"Cannot delete: job is in state '{status_response.current_status}'.")
else:
    delete_response = batch_service.delete(BATCH_ID)
    print(f"Deleted batch job: {delete_response.id}")
    print(f"Message: {delete_response.message}")
