from typing import Literal

MessageStatus = Literal["deleted", "delivered", "error", "pending", "requested"]

MESSAGE_STATUS_VALUES: set[MessageStatus] = {
    "deleted",
    "delivered",
    "error",
    "pending",
    "requested",
}


def check_message_status(value: str) -> MessageStatus:
    if value in MESSAGE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_STATUS_VALUES!r}")
