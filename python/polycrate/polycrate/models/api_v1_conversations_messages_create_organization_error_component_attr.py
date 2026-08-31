from typing import Literal

ApiV1ConversationsMessagesCreateOrganizationErrorComponentAttr = Literal["organization"]

API_V1_CONVERSATIONS_MESSAGES_CREATE_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsMessagesCreateOrganizationErrorComponentAttr
] = {
    "organization",
}


def check_api_v1_conversations_messages_create_organization_error_component_attr(
    value: str,
) -> ApiV1ConversationsMessagesCreateOrganizationErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_MESSAGES_CREATE_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_MESSAGES_CREATE_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
