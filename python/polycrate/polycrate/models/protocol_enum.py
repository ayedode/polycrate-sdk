from typing import Literal

ProtocolEnum = Literal["tcp", "udp"]

PROTOCOL_ENUM_VALUES: set[ProtocolEnum] = {
    "tcp",
    "udp",
}


def check_protocol_enum(value: str) -> ProtocolEnum:
    if value in PROTOCOL_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROTOCOL_ENUM_VALUES!r}")
