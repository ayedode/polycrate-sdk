from typing import Literal

ApiV1DatasourcesArchiveCreateDatasourceUrlErrorComponentAttr = Literal["datasource_url"]

API_V1_DATASOURCES_ARCHIVE_CREATE_DATASOURCE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesArchiveCreateDatasourceUrlErrorComponentAttr
] = {
    "datasource_url",
}


def check_api_v1_datasources_archive_create_datasource_url_error_component_attr(
    value: str,
) -> ApiV1DatasourcesArchiveCreateDatasourceUrlErrorComponentAttr:
    if value in API_V1_DATASOURCES_ARCHIVE_CREATE_DATASOURCE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_ARCHIVE_CREATE_DATASOURCE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
