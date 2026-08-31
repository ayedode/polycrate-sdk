from typing import Literal

ApiV1AssistantSessionsArchiveCreateStatusErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AssistantSessionsArchiveCreateStatusErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_assistant_sessions_archive_create_status_error_component_code(
    value: str,
) -> ApiV1AssistantSessionsArchiveCreateStatusErrorComponentCode:
    if value in API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
