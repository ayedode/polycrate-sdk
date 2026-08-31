from typing import Literal

ApiV1ConversationsConversationsListOrganizationErrorComponentAttr = Literal["organization"]

API_V1_CONVERSATIONS_CONVERSATIONS_LIST_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsConversationsListOrganizationErrorComponentAttr
] = {
    "organization",
}


def check_api_v1_conversations_conversations_list_organization_error_component_attr(
    value: str,
) -> ApiV1ConversationsConversationsListOrganizationErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_LIST_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_LIST_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
