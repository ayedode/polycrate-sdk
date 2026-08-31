from typing import Literal

ApiV1BackupsBackupsArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_backups_backups_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateKindErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
