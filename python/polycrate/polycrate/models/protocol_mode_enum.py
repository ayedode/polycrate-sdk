from typing import Literal

ProtocolModeEnum = Literal["http", "tcp"]

PROTOCOL_MODE_ENUM_VALUES: set[ProtocolModeEnum] = {
    "http",
    "tcp",
}


def check_protocol_mode_enum(value: str) -> ProtocolModeEnum:
    if value in PROTOCOL_MODE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROTOCOL_MODE_ENUM_VALUES!r}")
