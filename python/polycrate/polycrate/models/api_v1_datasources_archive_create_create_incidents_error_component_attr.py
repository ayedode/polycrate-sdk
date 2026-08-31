from typing import Literal

ApiV1DatasourcesArchiveCreateCreateIncidentsErrorComponentAttr = Literal["create_incidents"]

API_V1_DATASOURCES_ARCHIVE_CREATE_CREATE_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesArchiveCreateCreateIncidentsErrorComponentAttr
] = {
    "create_incidents",
}


def check_api_v1_datasources_archive_create_create_incidents_error_component_attr(
    value: str,
) -> ApiV1DatasourcesArchiveCreateCreateIncidentsErrorComponentAttr:
    if value in API_V1_DATASOURCES_ARCHIVE_CREATE_CREATE_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_ARCHIVE_CREATE_CREATE_INCIDENTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
