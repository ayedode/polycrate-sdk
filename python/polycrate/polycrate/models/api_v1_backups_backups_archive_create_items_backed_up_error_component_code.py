from typing import Literal

ApiV1BackupsBackupsArchiveCreateItemsBackedUpErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_ITEMS_BACKED_UP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateItemsBackedUpErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_backups_backups_archive_create_items_backed_up_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateItemsBackedUpErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_ITEMS_BACKED_UP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_ITEMS_BACKED_UP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
