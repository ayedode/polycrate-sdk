from typing import Literal

ApiV1DatasourcesUpdateDatasourceUrlErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DATASOURCES_UPDATE_DATASOURCE_URL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesUpdateDatasourceUrlErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_datasources_update_datasource_url_error_component_code(
    value: str,
) -> ApiV1DatasourcesUpdateDatasourceUrlErrorComponentCode:
    if value in API_V1_DATASOURCES_UPDATE_DATASOURCE_URL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_UPDATE_DATASOURCE_URL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
