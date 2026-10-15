from typing import Literal

EndpointDNSSpecProtocol = Literal["tcp", "udp"]

ENDPOINT_DNS_SPEC_PROTOCOL_VALUES: set[EndpointDNSSpecProtocol] = {
    "tcp",
    "udp",
}


def check_endpoint_dns_spec_protocol(value: str) -> EndpointDNSSpecProtocol:
    if value in ENDPOINT_DNS_SPEC_PROTOCOL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENDPOINT_DNS_SPEC_PROTOCOL_VALUES!r}")
