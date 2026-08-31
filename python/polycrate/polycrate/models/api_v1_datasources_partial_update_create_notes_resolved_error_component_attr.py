from typing import Literal

ApiV1DatasourcesPartialUpdateCreateNotesResolvedErrorComponentAttr = Literal["create_notes_resolved"]

API_V1_DATASOURCES_PARTIAL_UPDATE_CREATE_NOTES_RESOLVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesPartialUpdateCreateNotesResolvedErrorComponentAttr
] = {
    "create_notes_resolved",
}


def check_api_v1_datasources_partial_update_create_notes_resolved_error_component_attr(
    value: str,
) -> ApiV1DatasourcesPartialUpdateCreateNotesResolvedErrorComponentAttr:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_CREATE_NOTES_RESOLVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_CREATE_NOTES_RESOLVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
