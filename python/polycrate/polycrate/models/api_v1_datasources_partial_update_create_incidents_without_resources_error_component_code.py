from typing import Literal

ApiV1DatasourcesPartialUpdateCreateIncidentsWithoutResourcesErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_PARTIAL_UPDATE_CREATE_INCIDENTS_WITHOUT_RESOURCES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesPartialUpdateCreateIncidentsWithoutResourcesErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_partial_update_create_incidents_without_resources_error_component_code(
    value: str,
) -> ApiV1DatasourcesPartialUpdateCreateIncidentsWithoutResourcesErrorComponentCode:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_CREATE_INCIDENTS_WITHOUT_RESOURCES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_CREATE_INCIDENTS_WITHOUT_RESOURCES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
