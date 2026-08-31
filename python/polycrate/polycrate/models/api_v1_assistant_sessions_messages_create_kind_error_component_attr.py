from typing import Literal

ApiV1AssistantSessionsMessagesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsMessagesCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_assistant_sessions_messages_create_kind_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsMessagesCreateKindErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
