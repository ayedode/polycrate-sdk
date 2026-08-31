from typing import Literal

ApiV1DatasourcesRescanNotesCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_datasources_rescan_notes_create_criticality_error_component_attr(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateCriticalityErrorComponentAttr:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
