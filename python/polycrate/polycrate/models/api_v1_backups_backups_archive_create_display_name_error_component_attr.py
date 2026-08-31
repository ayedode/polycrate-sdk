from typing import Literal

ApiV1BackupsBackupsArchiveCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_backups_backups_archive_create_display_name_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateDisplayNameErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
