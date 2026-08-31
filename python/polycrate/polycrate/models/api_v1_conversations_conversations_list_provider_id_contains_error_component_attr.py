from typing import Literal

ApiV1ConversationsConversationsListProviderIdContainsErrorComponentAttr = Literal["provider_id_contains"]

API_V1_CONVERSATIONS_CONVERSATIONS_LIST_PROVIDER_ID_CONTAINS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsConversationsListProviderIdContainsErrorComponentAttr
] = {
    "provider_id_contains",
}


def check_api_v1_conversations_conversations_list_provider_id_contains_error_component_attr(
    value: str,
) -> ApiV1ConversationsConversationsListProviderIdContainsErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_LIST_PROVIDER_ID_CONTAINS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_LIST_PROVIDER_ID_CONTAINS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
