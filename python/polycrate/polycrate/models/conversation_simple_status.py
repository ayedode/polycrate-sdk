from typing import Literal

ConversationSimpleStatus = Literal["closed", "deleted", "waiting_for_operator", "waiting_for_user"]

CONVERSATION_SIMPLE_STATUS_VALUES: set[ConversationSimpleStatus] = {
    "closed",
    "deleted",
    "waiting_for_operator",
    "waiting_for_user",
}


def check_conversation_simple_status(value: str) -> ConversationSimpleStatus:
    if value in CONVERSATION_SIMPLE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_SIMPLE_STATUS_VALUES!r}")
