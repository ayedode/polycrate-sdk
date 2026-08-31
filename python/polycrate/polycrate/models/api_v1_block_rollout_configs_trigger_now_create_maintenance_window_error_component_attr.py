from typing import Literal

ApiV1BlockRolloutConfigsTriggerNowCreateMaintenanceWindowErrorComponentAttr = Literal["maintenance_window"]

API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_MAINTENANCE_WINDOW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsTriggerNowCreateMaintenanceWindowErrorComponentAttr
] = {
    "maintenance_window",
}


def check_api_v1_block_rollout_configs_trigger_now_create_maintenance_window_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsTriggerNowCreateMaintenanceWindowErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_MAINTENANCE_WINDOW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_TRIGGER_NOW_CREATE_MAINTENANCE_WINDOW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
