from typing import Literal

ApiV1AssistantSessionsCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_ASSISTANT_SESSIONS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_assistant_sessions_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
