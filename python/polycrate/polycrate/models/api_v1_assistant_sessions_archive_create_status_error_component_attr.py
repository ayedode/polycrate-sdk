from typing import Literal

ApiV1AssistantSessionsArchiveCreateStatusErrorComponentAttr = Literal["status"]

API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsArchiveCreateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_assistant_sessions_archive_create_status_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsArchiveCreateStatusErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
