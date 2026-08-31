from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateMaintenanceWindowErrorComponentAttr = Literal["maintenance_window"]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_MAINTENANCE_WINDOW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateMaintenanceWindowErrorComponentAttr
] = {
    "maintenance_window",
}


def check_api_v1_block_rollout_configs_partial_update_maintenance_window_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateMaintenanceWindowErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_MAINTENANCE_WINDOW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_MAINTENANCE_WINDOW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
