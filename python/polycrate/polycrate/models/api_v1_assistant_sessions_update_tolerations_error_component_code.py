from typing import Literal

ApiV1AssistantSessionsUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_ASSISTANT_SESSIONS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_assistant_sessions_update_tolerations_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsUpdateTolerationsErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
