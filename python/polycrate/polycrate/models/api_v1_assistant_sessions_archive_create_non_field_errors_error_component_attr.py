from typing import Literal

ApiV1AssistantSessionsArchiveCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsArchiveCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_assistant_sessions_archive_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsArchiveCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
