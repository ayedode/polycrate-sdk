from typing import Literal

ApiV1ConversationsConversationsCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsConversationsCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_conversations_conversations_create_kind_error_component_code(
    value: str,
) -> ApiV1ConversationsConversationsCreateKindErrorComponentCode:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
