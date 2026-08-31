# Polycrate SDKs

Typed HTTP clients for the [Polycrate API](https://docs.ayedo.de/polycrate/). One repository, three languages, all generated from the same OpenAPI description.

| Language | Package | Install from GitHub |
|---|---|---|
| Go | [`github.com/ayedode/polycrate-sdk/go`](https://github.com/ayedode/polycrate-sdk/tree/main/go) | `go get github.com/ayedode/polycrate-sdk/go@v<api-version>` |
| Python | [`polycrate`](https://github.com/ayedode/polycrate-sdk/tree/main/python/polycrate) | `pip install "polycrate @ git+https://github.com/ayedode/polycrate-sdk.git@v<api-version>#subdirectory=python/polycrate"` |
| JavaScript / TypeScript | [`@ayedo/polycrate-sdk`](https://github.com/ayedode/polycrate-sdk/tree/main/js) | `npm i github:ayedode/polycrate-sdk#v<api-version>:js` |

SDK versions match the Polycrate API version (for example API `0.33.0` → tag `v0.33.0`, package version `0.33.0`). These packages are not published to PyPI or npm. Pin the git tag to the API you talk to.

These clients wrap HTTP. They do not manage resource lifecycle or idempotency.

---

## Authentication

Protected endpoints expect a token:

```
Authorization: Bearer <token>
```

Create lasting keys in the Polycrate UI (the secret is shown once at creation):

| Key | Where in the UI |
|---|---|
| User | Account menu → **API Keys** (`/ui/accounts/api-keys/`) |
| Organization | Organization → **API Keys** tab |
| System | Administration → **System API Keys** (`/ui/administration/system-api-keys/`, staff only) |

All three use the same `Bearer` header. HTTP Basic on `/api/v1/…` is not sufficient.

Alternatively, a short-lived user token:

```
POST /api/login/
Content-Type: application/json

{"username":"<email>","password":"<password>"}
```

The response includes `token`.

Use the base URL of your Polycrate instance (no trailing path). Example: `https://app.ayedo.cloud`.

The live OpenAPI document is `GET /api/v1/schema/`. Interactive docs: `/api/docs/`.

---

## Go

Requires Go 1.23+.

```go
package main

import (
	"context"
	"fmt"
	"net/http"
	"os"

	polycrate "github.com/ayedode/polycrate-sdk/go"
)

func main() {
	token := os.Getenv("POLYCRATE_TOKEN")
	client, err := polycrate.NewClientWithResponses("https://app.ayedo.cloud",
		polycrate.WithRequestEditorFn(func(_ context.Context, req *http.Request) error {
			req.Header.Set("Authorization", "Bearer "+token)
			return nil
		}),
	)
	if err != nil {
		panic(err)
	}

	pageSize := 3
	resp, err := client.ApiV1WorkspacesListWithResponse(context.Background(), &polycrate.ApiV1WorkspacesListParams{
		PageSize: &pageSize,
	})
	if err != nil {
		panic(err)
	}
	if resp.JSON200 == nil {
		panic(fmt.Sprintf("HTTP %d", resp.StatusCode()))
	}
	fmt.Println(resp.JSON200.Count)
}
```

Each OpenAPI operation becomes a method on `Client` / `ClientWithResponses` (for example `ApiV1WorkspacesListWithResponse`). Successful JSON is on `JSON200` (or the matching status field). List names such as `WorkspaceList.Name` are pointers.

Install a tagged release (tag equals the API version):

```
go get github.com/ayedode/polycrate-sdk/go@v0.33.0
```

---

## Python

Requires Python 3.11+ and the dependencies `httpx` and `attrs`.

```python
from polycrate import AuthenticatedClient
from polycrate.api.api.api_v1_workspaces_list import sync_detailed

client = AuthenticatedClient(
    base_url="https://app.ayedo.cloud",
    token="...",
    prefix="Bearer",
)

resp = sync_detailed(client=client, page_size=3)
if resp.status_code != 200 or resp.parsed is None:
    raise SystemExit(f"HTTP {resp.status_code}")
print(resp.parsed.count, [ws.name for ws in resp.parsed.results])
```

Each path becomes a module under `polycrate.api.api` with four callables:

- `sync` / `sync_detailed` — blocking
- `asyncio` / `asyncio_detailed` — async

`*_detailed` always returns a `Response` (`status_code`, `content`, `parsed`). Use `AuthenticatedClient` for token auth and `Client` for public endpoints.

Install from GitHub (tag equals the API version):

```
pip install "polycrate @ git+https://github.com/ayedode/polycrate-sdk.git@v0.33.0#subdirectory=python/polycrate"
```

From a local clone: `pip install ./python/polycrate`.

---

## JavaScript / TypeScript

ESM. The package ships TypeScript sources (`js/src`).

```ts
import { OpenAPI, apiV1WorkspacesList } from "@ayedo/polycrate-sdk";

OpenAPI.BASE = "https://app.ayedo.cloud";
OpenAPI.TOKEN = process.env.POLYCRATE_TOKEN;

const page = await apiV1WorkspacesList({ pageSize: 3 });
console.log(page.count, page.results.map((ws) => ws.name));
```

Set `OpenAPI.TOKEN` once. The client sends `Authorization: Bearer`. Every operation is a named function (`apiV1WorkspacesList`, `apiV1OrganizationsList`, …). Query fields use camelCase (`pageSize`).

Install from GitHub (tag equals the API version):

```
npm i github:ayedode/polycrate-sdk#v0.33.0:js
```

From a local clone: `npm i ./js`. The package ships TypeScript sources; there is no separate build.

---

## What this repository contains

```
go/                 Go module (package polycrate)
python/polycrate/   Python package (import polycrate)
js/                 npm package @ayedo/polycrate-sdk
```

---

## Support

This repository is generated. Pull requests and GitHub issues are not accepted.

Email [support@ayedo.de](mailto:support@ayedo.de) with the SDK language, version, and a minimal request that shows the problem.

---

## License

Apache License 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

