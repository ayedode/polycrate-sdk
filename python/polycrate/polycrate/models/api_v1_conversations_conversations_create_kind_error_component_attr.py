from typing import Literal

ApiV1ConversationsConversationsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConversationsConversationsCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_conversations_conversations_create_kind_error_component_attr(
    value: str,
) -> ApiV1ConversationsConversationsCreateKindErrorComponentAttr:
    if value in API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONVERSATIONS_CONVERSATIONS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
