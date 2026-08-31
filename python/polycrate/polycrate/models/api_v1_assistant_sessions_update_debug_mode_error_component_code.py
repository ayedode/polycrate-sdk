from typing import Literal

ApiV1AssistantSessionsUpdateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_ASSISTANT_SESSIONS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsUpdateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_assistant_sessions_update_debug_mode_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsUpdateDebugModeErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
