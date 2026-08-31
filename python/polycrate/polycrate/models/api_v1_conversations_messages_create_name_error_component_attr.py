from typing import Literal

ApiV1ConversationsMessagesCreateNameErrorComponentAttr = Literal["name"]

API_V1_CONVERSATIONS_MESSAGES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_conversations_messages_create_name_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesCreateNameErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
