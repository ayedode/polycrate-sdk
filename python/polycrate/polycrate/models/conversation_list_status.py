from typing import Literal

ConversationListStatus = Literal["closed", "deleted", "waiting_for_operator", "waiting_for_user"]

CONVERSATION_LIST_STATUS_VALUES: set[ConversationListStatus] = {
    "closed",
    "deleted",
    "waiting_for_operator",
    "waiting_for_user",
}


def check_conversation_list_status(value: str) -> ConversationListStatus:
    if value in CONVERSATION_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONVERSATION_LIST_STATUS_VALUES!r}")
