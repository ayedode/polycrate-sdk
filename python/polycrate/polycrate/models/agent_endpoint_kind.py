from typing import Literal

AgentEndpointKind = Literal["dns", "http", "icmp", "tcp"]

AGENT_ENDPOINT_KIND_VALUES: set[AgentEndpointKind] = {
    "dns",
    "http",
    "icmp",
    "tcp",
}


def check_agent_endpoint_kind(value: str) -> AgentEndpointKind:
    if value in AGENT_ENDPOINT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENT_ENDPOINT_KIND_VALUES!r}")
