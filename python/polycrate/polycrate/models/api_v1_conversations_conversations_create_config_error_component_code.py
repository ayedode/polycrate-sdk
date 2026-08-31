from typing import Literal

ApiV1ConversationsConversationsCreateConfigErrorComponentCode = Literal["invalid", "null"]

API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsConversationsCreateConfigErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_conversations_conversations_create_config_error_component_code(
    value: str,
) -> ApiV1ConversationsConversationsCreateConfigErrorComponentCode:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
