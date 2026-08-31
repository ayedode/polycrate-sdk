from typing import Literal

ApiV1DatasourcesSyncCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_SYNC_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesSyncCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_sync_create_platform_service_error_component_code(
    value: str,
) -> ApiV1DatasourcesSyncCreatePlatformServiceErrorComponentCode:
    if value in API_V1_DATASOURCES_SYNC_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_SYNC_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
