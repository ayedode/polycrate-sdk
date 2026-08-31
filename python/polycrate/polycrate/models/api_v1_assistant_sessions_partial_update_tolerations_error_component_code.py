from typing import Literal

ApiV1AssistantSessionsPartialUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsPartialUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_assistant_sessions_partial_update_tolerations_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsPartialUpdateTolerationsErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
