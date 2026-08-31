from typing import Literal

ApiV1AssistantSessionsMessagesCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsMessagesCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_assistant_sessions_messages_create_labels_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsMessagesCreateLabelsErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
