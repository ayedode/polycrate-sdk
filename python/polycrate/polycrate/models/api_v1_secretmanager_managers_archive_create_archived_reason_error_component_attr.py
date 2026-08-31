from typing import Literal

ApiV1SecretmanagerManagersArchiveCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersArchiveCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_secretmanager_managers_archive_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersArchiveCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
