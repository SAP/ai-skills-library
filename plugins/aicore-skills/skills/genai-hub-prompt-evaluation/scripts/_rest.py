# /// script
# dependencies = ["sap-ai-sdk-core>=3.3.0", "requests>=2.31.0"]
# ///
"""
Shared helpers for prompt-evaluation scripts.

The SAP AI Core evaluation endpoints (/lm/evaluationMetrics, /registry/v2/orchestrationConfigs,
tag-filtered /lm/metrics) are not exposed by the SDK, so these scripts call them over raw REST
using the credentials the SDK already resolves from the environment. This mirrors the pattern in
skills/genai-hub-tabular-orchestration/scripts/*.

Import from a sibling script:
    from _rest import get_rest_context, request

`base_url` returned here always ends in /v2. If AICORE_BASE_URL does not include /v2, it is
appended automatically — matching the behaviour of the SDK's own high-level methods.
"""

import sys


def get_client(resource_group=None):
    """Initialise the AI Core client from the environment."""
    try:
        from ai_core_sdk.ai_core_v2_client import AICoreV2Client
    except ImportError:
        print(
            'ERROR: sap-ai-sdk-core not installed. Run: uv add "sap-ai-sdk-core>=3.3.0"',
            file=sys.stderr,
        )
        sys.exit(1)
    try:
        kwargs = {}
        if resource_group:
            kwargs["resource_group"] = resource_group
        return AICoreV2Client.from_env(
            read_timeout=15, connect_timeout=15, client_type="AI Core Skills", **kwargs
        )
    except Exception as e:
        print(
            f"ERROR: failed to initialise AI Core client ({type(e).__name__}). "
            "Check that AICORE_AUTH_URL, AICORE_CLIENT_ID, AICORE_CLIENT_SECRET, "
            "AICORE_BASE_URL, and AICORE_RESOURCE_GROUP are set correctly.",
            file=sys.stderr,
        )
        sys.exit(1)


def get_rest_context(resource_group=None):
    """Return (base_url, headers) for raw REST calls against AI Core.

    base_url already ends in /v2. headers carry the bearer token, resource group, and JSON
    content type. Token values are never printed.
    """
    client = get_client(resource_group)
    rc = client.rest_client
    base_url = rc.base_url.rstrip("/")
    if not base_url.endswith("/v2"):
        base_url += "/v2"
    rg = rc.headers.get("AI-Resource-Group", resource_group or "default")
    headers = {
        "Authorization": rc.get_token(),
        "AI-Resource-Group": rg,
        "Content-Type": "application/json",
    }
    return base_url, headers


def request(method, url, headers, *, json_body=None, timeout=120):
    """Perform an HTTP request and return the parsed JSON body.

    Exits with a clear, credential-free error on transport failure or a non-2xx status.
    """
    import requests

    try:
        resp = requests.request(method, url, headers=headers, json=json_body, timeout=timeout)
    except Exception as e:
        print(f"ERROR: request to {url} failed ({type(e).__name__}). "
              "Check network connectivity and that AICORE_BASE_URL is reachable.",
              file=sys.stderr)
        sys.exit(1)

    if not resp.ok:
        # Response bodies here are API error payloads, not credentials.
        print(f"ERROR {resp.status_code}: {resp.text}", file=sys.stderr)
        sys.exit(1)

    if not resp.text:
        return {}
    try:
        return resp.json()
    except ValueError:
        return {"raw": resp.text}
