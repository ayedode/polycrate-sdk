from typing import Literal

ApiV1AssistantSessionsPartialUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsPartialUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_assistant_sessions_partial_update_platform_service_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsPartialUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
