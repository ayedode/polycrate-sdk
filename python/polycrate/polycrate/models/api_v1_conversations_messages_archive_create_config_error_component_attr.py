from typing import Literal

ApiV1ConversationsMessagesArchiveCreateConfigErrorComponentAttr = Literal["config"]

API_V1_CONVERSATIONS_MESSAGES_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesArchiveCreateConfigErrorComponentAttr
] = {
    "config",
}


def check_api_v1_conversations_messages_archive_create_config_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesArchiveCreateConfigErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
