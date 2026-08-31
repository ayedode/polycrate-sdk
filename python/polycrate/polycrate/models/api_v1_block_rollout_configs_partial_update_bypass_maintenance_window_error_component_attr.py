from typing import Literal

ApiV1BlockRolloutConfigsPartialUpdateBypassMaintenanceWindowErrorComponentAttr = Literal["bypass_maintenance_window"]

API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_BYPASS_MAINTENANCE_WINDOW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsPartialUpdateBypassMaintenanceWindowErrorComponentAttr
] = {
    "bypass_maintenance_window",
}


def check_api_v1_block_rollout_configs_partial_update_bypass_maintenance_window_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsPartialUpdateBypassMaintenanceWindowErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_BYPASS_MAINTENANCE_WINDOW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_PARTIAL_UPDATE_BYPASS_MAINTENANCE_WINDOW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
