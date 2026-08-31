from typing import Literal

ApiV1AssistantSessionsListKindItem = Literal["generic"]

API_V1_ASSISTANT_SESSIONS_LIST_KIND_ITEM_VALUES: set[ApiV1AssistantSessionsListKindItem] = {
    "generic",
}


def check_api_v1_assistant_sessions_list_kind_item(value: str) -> ApiV1AssistantSessionsListKindItem:
    if value in API_V1_ASSISTANT_SESSIONS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_LIST_KIND_ITEM_VALUES!r}")
