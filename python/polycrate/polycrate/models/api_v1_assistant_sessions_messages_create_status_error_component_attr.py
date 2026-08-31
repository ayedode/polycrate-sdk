from typing import Literal

ApiV1AssistantSessionsMessagesCreateStatusErrorComponentAttr = Literal["status"]

API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsMessagesCreateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_assistant_sessions_messages_create_status_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsMessagesCreateStatusErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
