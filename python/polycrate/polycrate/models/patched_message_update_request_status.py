from typing import Literal

PatchedMessageUpdateRequestStatus = Literal["deleted", "delivered", "error", "pending", "requested"]

PATCHED_MESSAGE_UPDATE_REQUEST_STATUS_VALUES: set[PatchedMessageUpdateRequestStatus] = {
    "deleted",
    "delivered",
    "error",
    "pending",
    "requested",
}


def check_patched_message_update_request_status(value: str) -> PatchedMessageUpdateRequestStatus:
    if value in PATCHED_MESSAGE_UPDATE_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_MESSAGE_UPDATE_REQUEST_STATUS_VALUES!r}")
