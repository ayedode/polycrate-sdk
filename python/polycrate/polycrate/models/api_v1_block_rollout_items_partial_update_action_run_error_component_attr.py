from typing import Literal

ApiV1BlockRolloutItemsPartialUpdateActionRunErrorComponentAttr = Literal["action_run"]

API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_ACTION_RUN_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsPartialUpdateActionRunErrorComponentAttr
] = {
    "action_run",
}


def check_api_v1_block_rollout_items_partial_update_action_run_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsPartialUpdateActionRunErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_ACTION_RUN_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_ACTION_RUN_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
