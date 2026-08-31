from typing import Literal

ApiV1DatasourcesSyncCreateIsEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_SYNC_CREATE_IS_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesSyncCreateIsEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_sync_create_is_enabled_error_component_code(
    value: str,
) -> ApiV1DatasourcesSyncCreateIsEnabledErrorComponentCode:
    if value in API_V1_DATASOURCES_SYNC_CREATE_IS_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_IS_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
