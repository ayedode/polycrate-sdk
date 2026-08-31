from typing import Literal

ApiV1DatasourcesCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_create_platform_service_error_component_code(
    value: str,
) -> ApiV1DatasourcesCreatePlatformServiceErrorComponentCode:
    if value in API_V1_DATASOURCES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
