from typing import Literal

ApiV1AssistantSessionsUpdateStatusErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ASSISTANT_SESSIONS_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsUpdateStatusErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_assistant_sessions_update_status_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsUpdateStatusErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
