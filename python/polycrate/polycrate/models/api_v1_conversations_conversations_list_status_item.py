from typing import Literal

ApiV1ConversationsConversationsListStatusItem = Literal["closed", "deleted", "waiting_for_operator", "waiting_for_user"]

API_V1_CONVERSATIONS_CONVERSATIONS_LIST_STATUS_ITEM_VALUES: set[ApiV1ConversationsConversationsListStatusItem] = {
    "closed",
    "deleted",
    "waiting_for_operator",
    "waiting_for_user",
}


def check_api_v1_conversations_conversations_list_status_item(
    value: str,
) -> ApiV1ConversationsConversationsListStatusItem:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_LIST_STATUS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_LIST_STATUS_ITEM_VALUES!r}"
    )
