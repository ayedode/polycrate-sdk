from typing import Literal

ApiV1AssistantSessionsCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_ASSISTANT_SESSIONS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_assistant_sessions_create_criticality_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsCreateCriticalityErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
