from typing import Literal

ApiV1AssistantSessionsListSearchErrorComponentAttr = Literal["search"]

API_V1_ASSISTANT_SESSIONS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_assistant_sessions_list_search_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsListSearchErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
