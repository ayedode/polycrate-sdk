from typing import Literal

MessageStatusEnum = Literal["deleted", "delivered", "error", "pending", "requested"]

MESSAGE_STATUS_ENUM_VALUES: set[MessageStatusEnum] = {
    "deleted",
    "delivered",
    "error",
    "pending",
    "requested",
}


def check_message_status_enum(value: str) -> MessageStatusEnum:
    if value in MESSAGE_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_STATUS_ENUM_VALUES!r}")
