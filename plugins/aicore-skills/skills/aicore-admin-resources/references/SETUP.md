# AI Core Credential Setup

## Prerequisites

- An SAP BTP subaccount with the AI Core service enabled
- A service key for the AI Core instance

## Step 1: Install the AI Core SDK CLI

```bash
uv add "sap-ai-sdk-core"
```

## Step 2: Configure credentials

### Option A — Interactive CLI (recommended for local dev)

```bash
aicore configure
```

This writes credentials to `~/.aicore/config.json` (You can change the directory where the config file is located by setting the `AICORE_HOME` environment variable.). Follow the prompts:

- **Auth URL**: The `url` field from your service key + `/oauth/token`
- **Client ID**: `clientid` from the service key
- **Client Secret**: `clientsecret` from the service key
- **Base URL**: `serviceurls.AI_API_URL` from the service key (must end in `/v2`)
- **Resource Group**: the resource group to use for API calls (e.g. `default`, `my-team`). Run `uv run scripts/check_setup.py` to confirm the configured value.

Run `aicore configure --help` for full options.

### Option B — Environment variables

```bash
export AICORE_AUTH_URL="https://<subdomain>.authentication.<region>.hana.ondemand.com/oauth/token"
export AICORE_CLIENT_ID="<clientid from service key>"
export AICORE_CLIENT_SECRET="<clientsecret from service key>"
export AICORE_BASE_URL="https://api.ai.<region>.cfapps.<provider>.hana.ondemand.com/v2"
export AICORE_RESOURCE_GROUP="<your-resource-group>"
```

Add to `~/.zshrc` or `~/.bashrc` for persistence, or use a `.env` file with `python-dotenv`.

### Option C — Profile config file

Create `~/.aicore/config.json`:

```json
{
  "AICORE_AUTH_URL": "https://<subdomain>.authentication.<region>.hana.ondemand.com/oauth/token",
  "AICORE_CLIENT_ID": "<clientid>",
  "AICORE_CLIENT_SECRET": "<clientsecret>",
  "AICORE_BASE_URL": "https://api.ai.<region>.cfapps.<provider>.hana.ondemand.com/v2",
  "AICORE_RESOURCE_GROUP": "<your-resource-group>"
}
```

Use a named profile by setting `AICORE_PROFILE=<name>` and saving as `~/.aicore/config_<name>.json`.

## Step 3: Verify

```bash
uv run scripts/check_setup.py
```

Expected output:

```json
{
  "status": "ok",
  "resource_group": "<your-resource-group>"
}
```

## Common Errors

| Error                      | Cause                                  | Fix                                                                                  |
| -------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------ |
| `401 Unauthorized`         | Wrong client_id/secret                 | Re-run `aicore configure`                                                            |
| `404 Not Found`            | `AICORE_BASE_URL` missing `/v2` suffix | Append `/v2` to the URL                                                              |
| `Resource group not found` | Group doesn't exist in AI Core         | Create it in AI Core Launchpad or contact admin                                      |
| `No credentials found`     | Env vars not set                       | Set `AICORE_AUTH_URL`, `AICORE_CLIENT_ID`, `AICORE_CLIENT_SECRET`, `AICORE_BASE_URL` |

## X.509 Certificate Authentication (alternative to client secret)

```bash
export AICORE_CERT_FILE_PATH="/path/to/cert.pem"
export AICORE_KEY_FILE_PATH="/path/to/key.pem"
```

Or inline:

```bash
export AICORE_CERT_STR="<certificate content>"
export AICORE_KEY_STR="<private key content>"
```
