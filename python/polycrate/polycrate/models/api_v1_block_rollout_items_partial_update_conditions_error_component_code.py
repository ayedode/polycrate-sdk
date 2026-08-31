from typing import Literal

ApiV1BlockRolloutItemsPartialUpdateConditionsErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_CONDITIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsPartialUpdateConditionsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollout_items_partial_update_conditions_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsPartialUpdateConditionsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_CONDITIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_CONDITIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
