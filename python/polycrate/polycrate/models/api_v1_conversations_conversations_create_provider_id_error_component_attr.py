from typing import Literal

ApiV1ConversationsConversationsCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsConversationsCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_conversations_conversations_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1ConversationsConversationsCreateProviderIdErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
