from typing import Literal

ApiV1BackupsBackupsArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_backups_backups_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
