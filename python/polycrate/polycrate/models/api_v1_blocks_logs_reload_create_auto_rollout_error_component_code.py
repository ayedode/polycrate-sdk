from typing import Literal

ApiV1BlocksLogsReloadCreateAutoRolloutErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_AUTO_ROLLOUT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksLogsReloadCreateAutoRolloutErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_logs_reload_create_auto_rollout_error_component_code(
    value: str,
) -> ApiV1BlocksLogsReloadCreateAutoRolloutErrorComponentCode:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_AUTO_ROLLOUT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_AUTO_ROLLOUT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
