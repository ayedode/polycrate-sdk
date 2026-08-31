from typing import Literal

ApiV1ConversationsMessagesUpdateConfigErrorComponentAttr = Literal["config"]

API_V1_CONVERSATIONS_MESSAGES_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesUpdateConfigErrorComponentAttr
] = {
    "config",
}


def check_api_v1_conversations_messages_update_config_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesUpdateConfigErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
