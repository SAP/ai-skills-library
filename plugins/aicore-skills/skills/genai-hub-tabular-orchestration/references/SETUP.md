# BTP CLI Setup

## Step 1: Install BTP CLI

**macOS (Homebrew):**
```bash
brew install btp-cli
```

**Windows (winget):**
```bash
winget install SAP.btpcli
```

**Linux / manual install:**
Download the binary from https://tools.hana.ondemand.com/#cloud-btp, extract it, and add it to
your `PATH`.

Verify:

```bash
btp version
```

---

## Step 2: Log in via SSO

Choose the login command based on your landscape:

**Canary / internal landscapes** (hostname contains `canary`):
```bash
btp login --sso --url https://cpcli.cf.sap.hana.ondemand.com
```

**Live / external landscapes:**
```bash
btp login --sso
```

A browser window opens for SSO authentication. If no browser is available, copy the URL printed
to stdout and open it manually.

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `Error connecting to server` / `no such host` | Wrong CLI server URL | For internal landscapes use `--url https://cpcli.cf.sap.hana.ondemand.com` |
| `btp: command not found` | CLI not on PATH | Re-check install and PATH |
| `UNAUTHENTICATED` | Not logged in | Run `btp login --sso` |
