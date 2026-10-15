from typing import Literal

LbiV2ListenerProtocol = Literal["GRPC", "HTTP", "HTTPS", "TCP", "TLS"]

LBI_V2_LISTENER_PROTOCOL_VALUES: set[LbiV2ListenerProtocol] = {
    "GRPC",
    "HTTP",
    "HTTPS",
    "TCP",
    "TLS",
}


def check_lbi_v2_listener_protocol(value: str) -> LbiV2ListenerProtocol:
    if value in LBI_V2_LISTENER_PROTOCOL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LBI_V2_LISTENER_PROTOCOL_VALUES!r}")
