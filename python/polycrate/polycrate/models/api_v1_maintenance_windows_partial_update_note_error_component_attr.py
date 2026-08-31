from typing import Literal

ApiV1MaintenanceWindowsPartialUpdateNoteErrorComponentAttr = Literal["note"]

API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_NOTE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenanceWindowsPartialUpdateNoteErrorComponentAttr
] = {
    "note",
}


def check_api_v1_maintenance_windows_partial_update_note_error_component_attr(
    value: str,
) -> ApiV1MaintenanceWindowsPartialUpdateNoteErrorComponentAttr:
    if value in API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_NOTE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCE_WINDOWS_PARTIAL_UPDATE_NOTE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
