from typing import Literal

ApiV1AssistantSessionsMessagesCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsMessagesCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_assistant_sessions_messages_create_platform_service_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsMessagesCreatePlatformServiceErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
