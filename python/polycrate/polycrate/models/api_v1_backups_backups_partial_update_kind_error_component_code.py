from typing import Literal

ApiV1BackupsBackupsPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_backups_backups_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsPartialUpdateKindErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
