from typing import Literal

ApiV1BlockRolloutItemsCreateRepairRunningErrorComponentAttr = Literal["repair_running"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_REPAIR_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsCreateRepairRunningErrorComponentAttr
] = {
    "repair_running",
}


def check_api_v1_block_rollout_items_create_repair_running_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsCreateRepairRunningErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_REPAIR_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_REPAIR_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
