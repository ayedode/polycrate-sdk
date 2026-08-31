from typing import Literal

ApiV1MaintenanceWindowsUpdateDescriptionErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_MAINTENANCE_WINDOWS_UPDATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsUpdateDescriptionErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_maintenance_windows_update_description_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateDescriptionErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
