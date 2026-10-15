from typing import Literal

PatchedConversationUpdateRequestStatus = Literal["closed", "deleted", "waiting_for_operator", "waiting_for_user"]

PATCHED_CONVERSATION_UPDATE_REQUEST_STATUS_VALUES: set[PatchedConversationUpdateRequestStatus] = {
    "closed",
    "deleted",
    "waiting_for_operator",
    "waiting_for_user",
}


def check_patched_conversation_update_request_status(value: str) -> PatchedConversationUpdateRequestStatus:
    if value in PATCHED_CONVERSATION_UPDATE_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CONVERSATION_UPDATE_REQUEST_STATUS_VALUES!r}"
    )
