from typing import Literal

ApiV1AssistantSessionsArchiveCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsArchiveCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_assistant_sessions_archive_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsArchiveCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
