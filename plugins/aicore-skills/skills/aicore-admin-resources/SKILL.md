---
name: aicore-admin-resources
description: >
  Verify and configure SAP AI Core credentials, retrieve auth tokens, and manage resource groups.
  WHEN: user wants to check if AI Core is set up, configure credentials, get a Bearer token,
  fix authentication errors, run a setup health check, or list, create, update, or delete
  resource groups.
  DO NOT USE FOR: managing deployments — use `aicore-lifecycle-management`; listing foundation models — use `genai-hub-foundation-models`.
compatibility: Requires Python 3.11+, uv, and sap-ai-sdk-core.
---

## Rules

1. Always run `check_setup.py` first when credentials are unknown or when any script fails with an auth error.
2. `AICORE_BASE_URL` must end in `/v2` — this is the single most common misconfiguration.
3. Never display or log the client secret or token value in clear text. Print only what the user needs (e.g. the resource group, not the full config).
4. X.509 certificate auth is an alternative to client secret — both are supported.

---

## Check Setup

Verifies credentials and prints the active resource group:

```bash
uv run scripts/check_setup.py
```

Expected output on success:

```json
{
  "status": "ok",
  "resource_group": "<your-resource-group>",
  "base_url": "https://api.ai.<region>...",
  "auth_url": "https://..."
}
```

If this fails, read `references/SETUP.md` for step-by-step credential configuration.

---

## Get Auth Token

Prints a raw Bearer token to stdout — useful for curl testing:

```bash
export TOKEN=$(uv run scripts/get_token.py)
```

Always capture the token into a variable. Never run `get_token.py` standalone or with `2>&1` — that prints the raw JWT into the conversation. The success message already goes to stderr cleanly; `$()` capture gives only the bare token.

---

## Configure Credentials

Three options — see `references/SETUP.md` for the full guide:

| Option                        | Command / Action                                                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Interactive CLI (recommended) | `aicore configure`                                                                                            |
| Environment variables         | Set `AICORE_AUTH_URL`, `AICORE_CLIENT_ID`, `AICORE_CLIENT_SECRET`, `AICORE_BASE_URL`, `AICORE_RESOURCE_GROUP` |
| Profile config file           | Create `~/.aicore/config.json`                                                                                |

---

## Common Errors

| Error                      | Fix                                                   |
| -------------------------- | ----------------------------------------------------- |
| `401 Unauthorized`         | Re-run `aicore configure` — wrong client_id or secret |
| `404 Not Found`            | Append `/v2` to `AICORE_BASE_URL`                     |
| `Resource group not found` | Create it in AI Core Launchpad or contact admin       |
| `No credentials found`     | Set the required env vars or run `aicore configure`   |

---

## Switch Profiles (Multi-Landscape)

When working across multiple landscapes, credentials live as `config_<profile>.json` files under `AICORE_HOME` (default: `~/.aicore`). Because the shell environment is clean on each agent run, the profile must be set before the agent starts or inline with each command.

**Option 1 — set in your shell before starting the agent:**
```bash
export AICORE_HOME=/path/to/credentials  # only needed if not ~/.aicore
export AICORE_PROFILE=<profile>
# then start the agent — it inherits the env vars
```

**Option 2 — source and run in one shell (for agent use):**
```bash
source scripts/set_profile.sh <profile> && uv run scripts/check_setup.py
```

**Option 3 — inline per command:**
```bash
AICORE_PROFILE=<profile> uv run scripts/check_setup.py
```

To list available profiles:
```bash
source scripts/set_profile.sh
```

---

## Manage Resource Groups

```bash
# List all resource groups:
uv run scripts/list_resource_groups.py

# Show detailed view (includes labels):
uv run scripts/list_resource_groups.py --response-format detailed

# JSON output:
uv run scripts/list_resource_groups.py --json

# Inspect a single resource group:
uv run scripts/list_resource_groups.py --resource-group-id <id>

# Create a resource group:
uv run scripts/create_resource_group.py --id <id>

# Create with labels (keys must be prefixed ext.ai.sap.com/ or scenarios.ai.sap.com/):
uv run scripts/create_resource_group.py --id <id> --label ext.ai.sap.com/team=data --label ext.ai.sap.com/env=prod

# Update labels (replaces the full label set):
uv run scripts/patch_resource_group.py --id <id> --label ext.ai.sap.com/team=data

# Delete a resource group (--confirm is required):
uv run scripts/delete_resource_group.py --id <id> --confirm
```

Note: Resource group IDs must be 3–10 lowercase alphanumeric characters (hyphens allowed, not at start/end). Label keys must use the prefix `ext.ai.sap.com/` or `scenarios.ai.sap.com/` — bare keys like `team=data` will be rejected with a 400 error. Deletion may return 409 ("Conflicting ongoing action") immediately after creation while provisioning completes — retry after a short wait.

---

## Handoffs

- **Ready to manage deployments?** → invoke `aicore-lifecycle-management`
- **Need to list available models?** → invoke `genai-hub-foundation-models`

---

## When to Load Reference Files

| Trigger                                     | Load                  |
| ------------------------------------------- | --------------------- |
| Any credential/auth error or setup question | `references/SETUP.md` |

