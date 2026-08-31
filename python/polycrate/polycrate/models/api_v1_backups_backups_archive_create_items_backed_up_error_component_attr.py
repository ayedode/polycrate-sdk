from typing import Literal

ApiV1BackupsBackupsArchiveCreateItemsBackedUpErrorComponentAttr = Literal["items_backed_up"]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_ITEMS_BACKED_UP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateItemsBackedUpErrorComponentAttr
] = {
    "items_backed_up",
}


def check_api_v1_backups_backups_archive_create_items_backed_up_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateItemsBackedUpErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_ITEMS_BACKED_UP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_ITEMS_BACKED_UP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
