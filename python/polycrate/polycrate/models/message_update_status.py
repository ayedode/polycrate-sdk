from typing import Literal

MessageUpdateStatus = Literal["deleted", "delivered", "error", "pending", "requested"]

MESSAGE_UPDATE_STATUS_VALUES: set[MessageUpdateStatus] = {
    "deleted",
    "delivered",
    "error",
    "pending",
    "requested",
}


def check_message_update_status(value: str) -> MessageUpdateStatus:
    if value in MESSAGE_UPDATE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_UPDATE_STATUS_VALUES!r}")
