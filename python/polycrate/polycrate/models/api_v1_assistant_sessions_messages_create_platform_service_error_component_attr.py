from typing import Literal

ApiV1AssistantSessionsMessagesCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsMessagesCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_assistant_sessions_messages_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsMessagesCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_MESSAGES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
