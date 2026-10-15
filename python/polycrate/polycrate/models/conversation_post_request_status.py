from typing import Literal

ConversationPostRequestStatus = Literal["closed", "deleted", "waiting_for_operator", "waiting_for_user"]

CONVERSATION_POST_REQUEST_STATUS_VALUES: set[ConversationPostRequestStatus] = {
    "closed",
    "deleted",
    "waiting_for_operator",
    "waiting_for_user",
}


def check_conversation_post_request_status(value: str) -> ConversationPostRequestStatus:
    if value in CONVERSATION_POST_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_POST_REQUEST_STATUS_VALUES!r}")
