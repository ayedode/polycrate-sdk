from typing import Literal

ApiV1BlocksLogsReloadCreateConfigErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksLogsReloadCreateConfigErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_blocks_logs_reload_create_config_error_component_code(
    value: str,
) -> ApiV1BlocksLogsReloadCreateConfigErrorComponentCode:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
