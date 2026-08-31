from typing import Literal

ApiV1BlocksLogsReloadCreateConfigErrorComponentAttr = Literal["config"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateConfigErrorComponentAttr
] = {
    "config",
}


def check_api_v1_blocks_logs_reload_create_config_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateConfigErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
