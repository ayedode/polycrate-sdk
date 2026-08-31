from typing import Literal

ApiV1AssistantSessionsArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AssistantSessionsArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_assistant_sessions_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1AssistantSessionsArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ASSISTANT_SESSIONS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
