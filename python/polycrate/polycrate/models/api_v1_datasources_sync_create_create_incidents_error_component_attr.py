from typing import Literal

ApiV1DatasourcesSyncCreateCreateIncidentsErrorComponentAttr = Literal["create_incidents"]

API_V1_DATASOURCES_SYNC_CREATE_CREATE_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesSyncCreateCreateIncidentsErrorComponentAttr
] = {
    "create_incidents",
}


def check_api_v1_datasources_sync_create_create_incidents_error_component_attr(
    value: str,
) -> ApiV1DatasourcesSyncCreateCreateIncidentsErrorComponentAttr:
    if value in API_V1_DATASOURCES_SYNC_CREATE_CREATE_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_CREATE_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
