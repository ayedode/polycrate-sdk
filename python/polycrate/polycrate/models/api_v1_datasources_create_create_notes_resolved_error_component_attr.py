from typing import Literal

ApiV1DatasourcesCreateCreateNotesResolvedErrorComponentAttr = Literal["create_notes_resolved"]

API_V1_DATASOURCES_CREATE_CREATE_NOTES_RESOLVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesCreateCreateNotesResolvedErrorComponentAttr
] = {
    "create_notes_resolved",
}


def check_api_v1_datasources_create_create_notes_resolved_error_component_attr(
    value: str,
) -> ApiV1DatasourcesCreateCreateNotesResolvedErrorComponentAttr:
    if value in API_V1_DATASOURCES_CREATE_CREATE_NOTES_RESOLVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_CREATE_CREATE_NOTES_RESOLVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
