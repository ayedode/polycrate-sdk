from typing import Literal

ConversationStatusEnum = Literal["closed", "deleted", "waiting_for_operator", "waiting_for_user"]

CONVERSATION_STATUS_ENUM_VALUES: set[ConversationStatusEnum] = {
    "closed",
    "deleted",
    "waiting_for_operator",
    "waiting_for_user",
}


def check_conversation_status_enum(value: str) -> ConversationStatusEnum:
    if value in CONVERSATION_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_STATUS_ENUM_VALUES!r}")
