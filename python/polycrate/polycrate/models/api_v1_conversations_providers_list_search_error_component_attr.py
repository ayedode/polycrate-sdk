from typing import Literal

ApiV1ConversationsProvidersListSearchErrorComponentAttr = Literal["search"]

API_V1_CONVERSATIONS_PROVIDERS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsProvidersListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_conversations_providers_list_search_error_component_attr(
    value: str,
) -> ApiV1ConversationsProvidersListSearchErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_PROVIDERS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_PROVIDERS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
