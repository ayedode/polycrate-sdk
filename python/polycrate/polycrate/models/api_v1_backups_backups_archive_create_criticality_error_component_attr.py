from typing import Literal

ApiV1BackupsBackupsArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_backups_backups_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
