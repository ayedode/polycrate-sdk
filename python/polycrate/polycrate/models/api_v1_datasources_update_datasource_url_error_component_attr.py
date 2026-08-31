from typing import Literal

ApiV1DatasourcesUpdateDatasourceUrlErrorComponentAttr = Literal["datasource_url"]

API_V1_DATASOURCES_UPDATE_DATASOURCE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesUpdateDatasourceUrlErrorComponentAttr
] = {
    "datasource_url",
}


def check_api_v1_datasources_update_datasource_url_error_component_attr(
    value: str,
) -> ApiV1DatasourcesUpdateDatasourceUrlErrorComponentAttr:
    if value in API_V1_DATASOURCES_UPDATE_DATASOURCE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_UPDATE_DATASOURCE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
