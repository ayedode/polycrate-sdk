from typing import Literal

ApiV1DatasourcesRescanNotesCreateCreateIncidentsErrorComponentAttr = Literal["create_incidents"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_CREATE_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateCreateIncidentsErrorComponentAttr
] = {
    "create_incidents",
}


def check_api_v1_datasources_rescan_notes_create_create_incidents_error_component_attr(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateCreateIncidentsErrorComponentAttr:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_CREATE_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_CREATE_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
