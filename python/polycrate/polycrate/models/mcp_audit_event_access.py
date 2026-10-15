from typing import Literal

McpAuditEventAccess = Literal["read", "write"]

MCP_AUDIT_EVENT_ACCESS_VALUES: set[McpAuditEventAccess] = {
    "read",
    "write",
}


def check_mcp_audit_event_access(value: str) -> McpAuditEventAccess:
    if value in MCP_AUDIT_EVENT_ACCESS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MCP_AUDIT_EVENT_ACCESS_VALUES!r}")
