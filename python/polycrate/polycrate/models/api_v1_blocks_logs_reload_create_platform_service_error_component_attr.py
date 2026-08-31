from typing import Literal

ApiV1BlocksLogsReloadCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_blocks_logs_reload_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
