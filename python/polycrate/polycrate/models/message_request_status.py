from typing import Literal

MessageRequestStatus = Literal["deleted", "delivered", "error", "pending", "requested"]

MESSAGE_REQUEST_STATUS_VALUES: set[MessageRequestStatus] = {
    "deleted",
    "delivered",
    "error",
    "pending",
    "requested",
}


def check_message_request_status(value: str) -> MessageRequestStatus:
    if value in MESSAGE_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_REQUEST_STATUS_VALUES!r}")
