from typing import Literal

EndpointDNSSpecRequestProtocol = Literal["tcp", "udp"]

ENDPOINT_DNS_SPEC_REQUEST_PROTOCOL_VALUES: set[EndpointDNSSpecRequestProtocol] = {
    "tcp",
    "udp",
}


def check_endpoint_dns_spec_request_protocol(value: str) -> EndpointDNSSpecRequestProtocol:
    if value in ENDPOINT_DNS_SPEC_REQUEST_PROTOCOL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENDPOINT_DNS_SPEC_REQUEST_PROTOCOL_VALUES!r}")
