from typing import Literal

ApiV1ConversationsConversationsCreateMetaErrorComponentAttr = Literal["meta"]

API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_META_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsConversationsCreateMetaErrorComponentAttr
] = {
    "meta",
}


def check_api_v1_conversations_conversations_create_meta_error_component_attr(
    value: str,
) -> ApiV1ConversationsConversationsCreateMetaErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_META_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_META_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
