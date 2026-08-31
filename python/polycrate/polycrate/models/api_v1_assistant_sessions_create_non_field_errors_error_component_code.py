from typing import Literal

ApiV1AssistantSessionsCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_ASSISTANT_SESSIONS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_assistant_sessions_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
