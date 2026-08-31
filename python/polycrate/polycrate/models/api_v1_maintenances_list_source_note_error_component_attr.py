from typing import Literal

ApiV1MaintenancesListSourceNoteErrorComponentAttr = Literal["source_note"]

API_V1_MAINTENANCES_LIST_SOURCE_NOTE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1MaintenancesListSourceNoteErrorComponentAttr
] = {
    "source_note",
}


def check_api_v1_maintenances_list_source_note_error_component_attr(
    value: str,
) -> ApiV1MaintenancesListSourceNoteErrorComponentAttr:
    if value in API_V1_MAINTENANCES_LIST_SOURCE_NOTE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_MAINTENANCES_LIST_SOURCE_NOTE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
