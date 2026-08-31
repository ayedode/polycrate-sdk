from typing import Literal

ApiV1ConversationsConversationsUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_CONVERSATIONS_CONVERSATIONS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsConversationsUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_conversations_conversations_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1ConversationsConversationsUpdateProviderIdErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
