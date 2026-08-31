from typing import Literal

ApiV1DatasourcesRescanNotesCreateCreateIncidentsWithoutResourcesErrorComponentAttr = Literal[
    "create_incidents_without_resources"
]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_CREATE_INCIDENTS_WITHOUT_RESOURCES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateCreateIncidentsWithoutResourcesErrorComponentAttr
] = {
    "create_incidents_without_resources",
}


def check_api_v1_datasources_rescan_notes_create_create_incidents_without_resources_error_component_attr(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateCreateIncidentsWithoutResourcesErrorComponentAttr:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_CREATE_INCIDENTS_WITHOUT_RESOURCES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_CREATE_INCIDENTS_WITHOUT_RESOURCES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
