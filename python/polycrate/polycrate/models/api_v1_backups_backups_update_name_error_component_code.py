from typing import Literal

ApiV1BackupsBackupsUpdateNameErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "min_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_BACKUPS_BACKUPS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BackupsBackupsUpdateNameErrorComponentCode] = {
    "blank",
    "invalid",
    "max_length",
    "min_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_backups_backups_update_name_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsUpdateNameErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
