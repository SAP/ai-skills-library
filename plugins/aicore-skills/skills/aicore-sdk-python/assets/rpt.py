# File:    skills/aicore-sdk-python/assets/rpt.py
# Install: uv add sap-ai-sdk-gen
# Run:     uv run assets/rpt.py
#
# SAP-RPT relational/tabular prediction — regression (pydantic) and classification (dict).
# Credentials: run 'aicore configure' or see aicore-admin-resources/references/SETUP.md
# See: https://help.sap.com/docs/sap-ai-core/generative-ai/quick-start

from gen_ai_hub.proxy.native.sap import RPTRequest, PredictionConfig, TargetColumn, RPTClient

rows_regression = [
    {"PRODUCT": "Couch", "PRICE": 999.99, "ORDERDATE": "28-11-2025", "ID": "35", "DISCOUNT_RATE": "[PREDICT]"},
    {"PRODUCT": "Office Chair", "PRICE": 150.80, "ORDERDATE": "02-11-2025", "ID": "44", "DISCOUNT_RATE": 0.12},
    {"PRODUCT": "Server Rack", "PRICE": 2200.00, "ORDERDATE": "01-11-2025", "ID": "104", "DISCOUNT_RATE": 0.05},
    {"PRODUCT": "Standing Desk", "PRICE": 640.00, "ORDERDATE": "05-11-2025", "ID": "205", "DISCOUNT_RATE": 0.10},
    {"PRODUCT": "Monitor 27 inch", "PRICE": 289.99, "ORDERDATE": "08-11-2025", "ID": "306", "DISCOUNT_RATE": "[PREDICT]"},
]

client = RPTClient()
body = RPTRequest(
    prediction_config=PredictionConfig(
        target_columns=[TargetColumn(name="DISCOUNT_RATE", prediction_placeholder="[PREDICT]", task_type="regression")]
    ),
    rows=rows_regression
)
response = client.predict(body=body, model_name="sap-rpt-1.6")
print(response.predictions)

# With model_version
response = client.predict(body=body, model_name="sap-rpt-1.6", model_version="latest")
print(response.predictions)

# Classification via a plain dict request (columns + schema)
client = RPTClient()
example_request_by_columns_dict = {
    "prediction_config": {
        "target_columns": [{"name": "COSTCENTER", "prediction_placeholder": "[PREDICT]", "task_type": "classification"}]
    },
    "columns": {
        "PRODUCT": ["Couch", "Office Chair", "Server Rack"],
        "PRICE": [999.99, 150.8, 2200.00],
        "ORDERDATE": ["28-11-2025", "02-11-2025", "01-11-2025"],
        "ID": ["35", "44", "104"],
        "COSTCENTER": ["[PREDICT]", "Office Furniture", "Data Infrastructure"]
    },
    "data_schema": {
        "PRODUCT": {"dtype": "string"},
        "PRICE": {"dtype": "numeric"},
        "ORDERDATE": {"dtype": "date"},
        "ID": {"dtype": "string"},
        "COSTCENTER": {"dtype": "string"}
    }
}

response = client.predict(body=example_request_by_columns_dict, model_name="sap-rpt-1.6")
print(response.predictions)
