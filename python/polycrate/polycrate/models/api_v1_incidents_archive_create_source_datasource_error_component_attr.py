from typing import Literal

ApiV1IncidentsArchiveCreateSourceDatasourceErrorComponentAttr = Literal["source_datasource"]

API_V1_INCIDENTS_ARCHIVE_CREATE_SOURCE_DATASOURCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsArchiveCreateSourceDatasourceErrorComponentAttr
] = {
    "source_datasource",
}


def check_api_v1_incidents_archive_create_source_datasource_error_component_attr(
    value: str,
) -> ApiV1IncidentsArchiveCreateSourceDatasourceErrorComponentAttr:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_SOURCE_DATASOURCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_SOURCE_DATASOURCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
