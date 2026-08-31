from typing import Literal

ApiV1MaintenancesListSourceNoteErrorComponentCode = Literal["invalid_choice"]

API_V1_MAINTENANCES_LIST_SOURCE_NOTE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1MaintenancesListSourceNoteErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_maintenances_list_source_note_error_component_code(
    value: str,
) -> ApiV1MaintenancesListSourceNoteErrorComponentCode:
    if value in API_V1_MAINTENANCES_LIST_SOURCE_NOTE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_SOURCE_NOTE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
