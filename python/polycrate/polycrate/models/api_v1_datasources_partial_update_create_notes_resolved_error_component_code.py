from typing import Literal

ApiV1DatasourcesPartialUpdateCreateNotesResolvedErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_PARTIAL_UPDATE_CREATE_NOTES_RESOLVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesPartialUpdateCreateNotesResolvedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_partial_update_create_notes_resolved_error_component_code(
    value: str,
) -> ApiV1DatasourcesPartialUpdateCreateNotesResolvedErrorComponentCode:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_CREATE_NOTES_RESOLVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_CREATE_NOTES_RESOLVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
