from typing import Literal

ApiV1ConversationsMessagesUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_CONVERSATIONS_MESSAGES_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_conversations_messages_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesUpdateProviderIdErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
