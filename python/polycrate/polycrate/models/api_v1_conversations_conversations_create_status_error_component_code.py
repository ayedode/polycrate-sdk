from typing import Literal

ApiV1ConversationsConversationsCreateStatusErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsConversationsCreateStatusErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_conversations_conversations_create_status_error_component_code(
    value: str,
) -> ApiV1ConversationsConversationsCreateStatusErrorComponentCode:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
