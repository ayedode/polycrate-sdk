from typing import Literal

ApiV1BlockRolloutItemsPartialUpdateRolloutErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_ROLLOUT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsPartialUpdateRolloutErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_block_rollout_items_partial_update_rollout_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsPartialUpdateRolloutErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_ROLLOUT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_ROLLOUT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
