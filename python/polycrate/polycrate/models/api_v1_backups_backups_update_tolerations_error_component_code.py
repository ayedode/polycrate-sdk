from typing import Literal

ApiV1BackupsBackupsUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_BACKUPS_BACKUPS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_backups_backups_update_tolerations_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsUpdateTolerationsErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
