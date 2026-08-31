from typing import Literal

ApiV1ConversationsConversationsCreateNameErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsConversationsCreateNameErrorComponentCode
] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_conversations_conversations_create_name_error_component_code(
    value: str,
) -> ApiV1ConversationsConversationsCreateNameErrorComponentCode:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
