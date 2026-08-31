from typing import Literal

ApiV1BlockRolloutConfigsUpdateBypassMaintenanceWindowErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_BYPASS_MAINTENANCE_WINDOW_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateBypassMaintenanceWindowErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollout_configs_update_bypass_maintenance_window_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateBypassMaintenanceWindowErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_BYPASS_MAINTENANCE_WINDOW_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_BYPASS_MAINTENANCE_WINDOW_ERROR_COMPONENT_CODE_VALUES!r}"
    )
