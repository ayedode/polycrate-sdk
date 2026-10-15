from typing import Literal

ConversationUpdateStatus = Literal["closed", "deleted", "waiting_for_operator", "waiting_for_user"]

CONVERSATION_UPDATE_STATUS_VALUES: set[ConversationUpdateStatus] = {
    "closed",
    "deleted",
    "waiting_for_operator",
    "waiting_for_user",
}


def check_conversation_update_status(value: str) -> ConversationUpdateStatus:
    if value in CONVERSATION_UPDATE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_UPDATE_STATUS_VALUES!r}")
