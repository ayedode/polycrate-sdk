from typing import Literal

LbiV2ListenerRequestProtocol = Literal["GRPC", "HTTP", "HTTPS", "TCP", "TLS"]

LBI_V2_LISTENER_REQUEST_PROTOCOL_VALUES: set[LbiV2ListenerRequestProtocol] = {
    "GRPC",
    "HTTP",
    "HTTPS",
    "TCP",
    "TLS",
}


def check_lbi_v2_listener_request_protocol(value: str) -> LbiV2ListenerRequestProtocol:
    if value in LBI_V2_LISTENER_REQUEST_PROTOCOL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LBI_V2_LISTENER_REQUEST_PROTOCOL_VALUES!r}")
