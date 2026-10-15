from typing import Literal

ConversationUpdateRequestStatus = Literal["closed", "deleted", "waiting_for_operator", "waiting_for_user"]

CONVERSATION_UPDATE_REQUEST_STATUS_VALUES: set[ConversationUpdateRequestStatus] = {
    "closed",
    "deleted",
    "waiting_for_operator",
    "waiting_for_user",
}


def check_conversation_update_request_status(value: str) -> ConversationUpdateRequestStatus:
    if value in CONVERSATION_UPDATE_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_UPDATE_REQUEST_STATUS_VALUES!r}")
