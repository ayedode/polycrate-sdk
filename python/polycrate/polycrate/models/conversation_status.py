from typing import Literal

ConversationStatus = Literal["closed", "deleted", "waiting_for_operator", "waiting_for_user"]

CONVERSATION_STATUS_VALUES: set[ConversationStatus] = {
    "closed",
    "deleted",
    "waiting_for_operator",
    "waiting_for_user",
}


def check_conversation_status(value: str) -> ConversationStatus:
    if value in CONVERSATION_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_STATUS_VALUES!r}")
