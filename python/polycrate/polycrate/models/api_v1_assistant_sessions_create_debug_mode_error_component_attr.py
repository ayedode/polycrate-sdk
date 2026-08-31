from typing import Literal

ApiV1AssistantSessionsCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_ASSISTANT_SESSIONS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_assistant_sessions_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsCreateDebugModeErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
