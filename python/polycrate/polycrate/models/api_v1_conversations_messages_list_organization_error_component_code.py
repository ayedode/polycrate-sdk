from typing import Literal

ApiV1ConversationsMessagesListOrganizationErrorComponentCode = Literal["invalid_choice"]

API_V1_CONVERSATIONS_MESSAGES_LIST_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConversationsMessagesListOrganizationErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_conversations_messages_list_organization_error_component_code(
    value: str,
) -> ApiV1ConversationsMessagesListOrganizationErrorComponentCode:
    if value in API_V1_CONVERSATIONS_MESSAGES_LIST_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_LIST_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
