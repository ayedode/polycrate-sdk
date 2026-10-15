from typing import Literal

MessageListStatus = Literal["deleted", "delivered", "error", "pending", "requested"]

MESSAGE_LIST_STATUS_VALUES: set[MessageListStatus] = {
    "deleted",
    "delivered",
    "error",
    "pending",
    "requested",
}


def check_message_list_status(value: str) -> MessageListStatus:
    if value in MESSAGE_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MESSAGE_LIST_STATUS_VALUES!r}")
