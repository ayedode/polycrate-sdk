from typing import Literal

ApiV1ConversationsConversationsUpdateMetaErrorComponentAttr = Literal["meta"]

API_V1_CONVERSATIONS_CONVERSATIONS_UPDATE_META_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsConversationsUpdateMetaErrorComponentAttr
] = {
    "meta",
}


def check_api_v1_conversations_conversations_update_meta_error_component_attr(
    value: str,
) -> ApiV1ConversationsConversationsUpdateMetaErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_UPDATE_META_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_UPDATE_META_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
