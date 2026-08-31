from typing import Literal

ApiV1AssistantSessionsMessagesCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsMessagesCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_assistant_sessions_messages_create_annotations_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsMessagesCreateAnnotationsErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
