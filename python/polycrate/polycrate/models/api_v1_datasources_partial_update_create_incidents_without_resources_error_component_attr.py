from typing import Literal

ApiV1DatasourcesPartialUpdateCreateIncidentsWithoutResourcesErrorComponentAttr = Literal[
    "create_incidents_without_resources"
]

API_V1_DATASOURCES_PARTIAL_UPDATE_CREATE_INCIDENTS_WITHOUT_RESOURCES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesPartialUpdateCreateIncidentsWithoutResourcesErrorComponentAttr
] = {
    "create_incidents_without_resources",
}


def check_api_v1_datasources_partial_update_create_incidents_without_resources_error_component_attr(
    value: str,
) -> ApiV1DatasourcesPartialUpdateCreateIncidentsWithoutResourcesErrorComponentAttr:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_CREATE_INCIDENTS_WITHOUT_RESOURCES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_CREATE_INCIDENTS_WITHOUT_RESOURCES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
