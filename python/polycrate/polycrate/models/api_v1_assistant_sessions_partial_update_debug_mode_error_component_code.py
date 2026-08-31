from typing import Literal

ApiV1AssistantSessionsPartialUpdateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsPartialUpdateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_assistant_sessions_partial_update_debug_mode_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsPartialUpdateDebugModeErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
