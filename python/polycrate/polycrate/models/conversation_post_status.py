from typing import Literal

ConversationPostStatus = Literal["closed", "deleted", "waiting_for_operator", "waiting_for_user"]

CONVERSATION_POST_STATUS_VALUES: set[ConversationPostStatus] = {
    "closed",
    "deleted",
    "waiting_for_operator",
    "waiting_for_user",
}


def check_conversation_post_status(value: str) -> ConversationPostStatus:
    if value in CONVERSATION_POST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_POST_STATUS_VALUES!r}")
