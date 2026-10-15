from typing import Literal

MessagePostStatus = Literal["deleted", "delivered", "error", "pending", "requested"]

MESSAGE_POST_STATUS_VALUES: set[MessagePostStatus] = {
    "deleted",
    "delivered",
    "error",
    "pending",
    "requested",
}


def check_message_post_status(value: str) -> MessagePostStatus:
    if value in MESSAGE_POST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_POST_STATUS_VALUES!r}")
