from typing import Literal

ApiV1BackupsBackupsPartialUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsPartialUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_backups_backups_partial_update_criticality_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsPartialUpdateCriticalityErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
