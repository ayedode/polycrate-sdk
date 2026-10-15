from typing import Literal

ConversationRequestStatus = Literal["closed", "deleted", "waiting_for_operator", "waiting_for_user"]

CONVERSATION_REQUEST_STATUS_VALUES: set[ConversationRequestStatus] = {
    "closed",
    "deleted",
    "waiting_for_operator",
    "waiting_for_user",
}


def check_conversation_request_status(value: str) -> ConversationRequestStatus:
    if value in CONVERSATION_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_REQUEST_STATUS_VALUES!r}")
