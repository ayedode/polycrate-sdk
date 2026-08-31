from typing import Literal

ApiV1MaintenanceWindowsUpdateNoteErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_MAINTENANCE_WINDOWS_UPDATE_NOTE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenanceWindowsUpdateNoteErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_maintenance_windows_update_note_error_component_code(
    value: str,
) -> ApiV1MaintenanceWindowsUpdateNoteErrorComponentCode:
    if value in API_V1_MAINTENANCE_WINDOWS_UPDATE_NOTE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_UPDATE_NOTE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
