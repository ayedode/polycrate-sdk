from typing import Literal

ApiV1ConversationsMessagesPartialUpdateConfigErrorComponentAttr = Literal["config"]

API_V1_CONVERSATIONS_MESSAGES_PARTIAL_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesPartialUpdateConfigErrorComponentAttr
] = {
    "config",
}


def check_api_v1_conversations_messages_partial_update_config_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesPartialUpdateConfigErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_PARTIAL_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_PARTIAL_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
