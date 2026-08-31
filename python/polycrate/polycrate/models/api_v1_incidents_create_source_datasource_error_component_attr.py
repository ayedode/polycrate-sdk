from typing import Literal

ApiV1IncidentsCreateSourceDatasourceErrorComponentAttr = Literal["source_datasource"]

API_V1_INCIDENTS_CREATE_SOURCE_DATASOURCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsCreateSourceDatasourceErrorComponentAttr
] = {
    "source_datasource",
}


def check_api_v1_incidents_create_source_datasource_error_component_attr(
    value: str,
) -> ApiV1IncidentsCreateSourceDatasourceErrorComponentAttr:
    if value in API_V1_INCIDENTS_CREATE_SOURCE_DATASOURCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_SOURCE_DATASOURCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
