from typing import Literal

ApiV1BlockRolloutConfigsUpdateMaintenanceWindowErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_MAINTENANCE_WINDOW_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateMaintenanceWindowErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_block_rollout_configs_update_maintenance_window_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateMaintenanceWindowErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_MAINTENANCE_WINDOW_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_MAINTENANCE_WINDOW_ERROR_COMPONENT_CODE_VALUES!r}"
    )
