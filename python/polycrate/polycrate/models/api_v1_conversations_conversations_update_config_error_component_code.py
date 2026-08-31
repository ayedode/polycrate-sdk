from typing import Literal

ApiV1ConversationsConversationsUpdateConfigErrorComponentCode = Literal["invalid", "null"]

API_V1_CONVERSATIONS_CONVERSATIONS_UPDATE_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsConversationsUpdateConfigErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_conversations_conversations_update_config_error_component_code(
    value: str,
) -> ApiV1ConversationsConversationsUpdateConfigErrorComponentCode:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_UPDATE_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_UPDATE_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
