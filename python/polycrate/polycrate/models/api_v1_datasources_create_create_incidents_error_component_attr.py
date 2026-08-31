from typing import Literal

ApiV1DatasourcesCreateCreateIncidentsErrorComponentAttr = Literal["create_incidents"]

API_V1_DATASOURCES_CREATE_CREATE_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesCreateCreateIncidentsErrorComponentAttr
] = {
    "create_incidents",
}


def check_api_v1_datasources_create_create_incidents_error_component_attr(
    value: str,
) -> ApiV1DatasourcesCreateCreateIncidentsErrorComponentAttr:
    if value in API_V1_DATASOURCES_CREATE_CREATE_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_CREATE_CREATE_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
