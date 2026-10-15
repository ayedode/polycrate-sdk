from typing import Literal

MessageUpdateRequestStatus = Literal["deleted", "delivered", "error", "pending", "requested"]

MESSAGE_UPDATE_REQUEST_STATUS_VALUES: set[MessageUpdateRequestStatus] = {
    "deleted",
    "delivered",
    "error",
    "pending",
    "requested",
}


def check_message_update_request_status(value: str) -> MessageUpdateRequestStatus:
    if value in MESSAGE_UPDATE_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_UPDATE_REQUEST_STATUS_VALUES!r}")
