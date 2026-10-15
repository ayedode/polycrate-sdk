from typing import Literal

McpAuditEventOutcome = Literal["denied", "error", "ok"]

MCP_AUDIT_EVENT_OUTCOME_VALUES: set[McpAuditEventOutcome] = {
    "denied",
    "error",
    "ok",
}


def check_mcp_audit_event_outcome(value: str) -> McpAuditEventOutcome:
    if value in MCP_AUDIT_EVENT_OUTCOME_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MCP_AUDIT_EVENT_OUTCOME_VALUES!r}")
