from typing import Literal

ApiV1ConversationsConversationsListProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_CONVERSATIONS_CONVERSATIONS_LIST_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsConversationsListProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_conversations_conversations_list_provider_id_error_component_attr(
    value: str,
) -> ApiV1ConversationsConversationsListProviderIdErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_LIST_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_LIST_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
