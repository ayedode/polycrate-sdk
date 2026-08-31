from typing import Literal

ApiV1DatasourcesCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_DATASOURCES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_datasources_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1DatasourcesCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_DATASOURCES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
