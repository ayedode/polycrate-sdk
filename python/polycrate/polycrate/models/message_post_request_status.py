from typing import Literal

MessagePostRequestStatus = Literal["deleted", "delivered", "error", "pending", "requested"]

MESSAGE_POST_REQUEST_STATUS_VALUES: set[MessagePostRequestStatus] = {
    "deleted",
    "delivered",
    "error",
    "pending",
    "requested",
}


def check_message_post_request_status(value: str) -> MessagePostRequestStatus:
    if value in MESSAGE_POST_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_POST_REQUEST_STATUS_VALUES!r}")
