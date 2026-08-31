from typing import Literal

ApiV1ConversationsConversationsPartialUpdateMetaErrorComponentCode = Literal["invalid", "null"]

API_V1_CONVERSATIONS_CONVERSATIONS_PARTIAL_UPDATE_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsConversationsPartialUpdateMetaErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_conversations_conversations_partial_update_meta_error_component_code(
    value: str,
) -> ApiV1ConversationsConversationsPartialUpdateMetaErrorComponentCode:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_PARTIAL_UPDATE_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_PARTIAL_UPDATE_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
