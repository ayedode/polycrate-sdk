from typing import Literal

ApiV1DatasourcesPartialUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_DATASOURCES_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesPartialUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_datasources_partial_update_platform_service_error_component_code(
    value: str,
) -> ApiV1DatasourcesPartialUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_DATASOURCES_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
