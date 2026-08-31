from typing import Literal

ApiV1ConversationsConversationsCreateNameErrorComponentAttr = Literal["name"]

API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsConversationsCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_conversations_conversations_create_name_error_component_attr(
    value: str,
) -> ApiV1ConversationsConversationsCreateNameErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
