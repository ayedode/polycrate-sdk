from typing import Literal

ApiV1IncidentsPartialUpdateSourceDatasourceErrorComponentAttr = Literal["source_datasource"]

API_V1_INCIDENTS_PARTIAL_UPDATE_SOURCE_DATASOURCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsPartialUpdateSourceDatasourceErrorComponentAttr
] = {
    "source_datasource",
}


def check_api_v1_incidents_partial_update_source_datasource_error_component_attr(
    value: str,
) -> ApiV1IncidentsPartialUpdateSourceDatasourceErrorComponentAttr:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_SOURCE_DATASOURCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_SOURCE_DATASOURCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
