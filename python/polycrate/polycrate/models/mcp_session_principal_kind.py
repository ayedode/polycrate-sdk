from typing import Literal

McpSessionPrincipalKind = Literal["microservice", "org_api_key", "system_api_key", "user"]

MCP_SESSION_PRINCIPAL_KIND_VALUES: set[McpSessionPrincipalKind] = {
    "microservice",
    "org_api_key",
    "system_api_key",
    "user",
}


def check_mcp_session_principal_kind(value: str) -> McpSessionPrincipalKind:
    if value in MCP_SESSION_PRINCIPAL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MCP_SESSION_PRINCIPAL_KIND_VALUES!r}")
