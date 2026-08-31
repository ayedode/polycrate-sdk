from typing import Literal

ApiV1BlockRolloutConfigsCreateMaintenanceWindowErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_MAINTENANCE_WINDOW_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsCreateMaintenanceWindowErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_block_rollout_configs_create_maintenance_window_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateMaintenanceWindowErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_MAINTENANCE_WINDOW_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_MAINTENANCE_WINDOW_ERROR_COMPONENT_CODE_VALUES!r}"
    )
