from typing import Literal

ApiV1BlockRolloutItemsUpdateRepairRunningErrorComponentAttr = Literal["repair_running"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_REPAIR_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsUpdateRepairRunningErrorComponentAttr
] = {
    "repair_running",
}


def check_api_v1_block_rollout_items_update_repair_running_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateRepairRunningErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_REPAIR_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_REPAIR_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
