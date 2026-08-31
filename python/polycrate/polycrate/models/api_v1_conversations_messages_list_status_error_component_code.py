from typing import Literal

ApiV1ConversationsMessagesListStatusErrorComponentCode = Literal["invalid_choice", "invalid_list"]

API_V1_CONVERSATIONS_MESSAGES_LIST_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsMessagesListStatusErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
}


def check_api_v1_conversations_messages_list_status_error_component_code(
    value: str,
) -> ApiV1ConversationsMessagesListStatusErrorComponentCode:
    if value in API_V1_CONVERSATIONS_MESSAGES_LIST_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_LIST_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
