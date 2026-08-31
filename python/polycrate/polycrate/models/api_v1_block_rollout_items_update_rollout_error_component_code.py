from typing import Literal

ApiV1BlockRolloutItemsUpdateRolloutErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_ROLLOUT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsUpdateRolloutErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_block_rollout_items_update_rollout_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateRolloutErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_ROLLOUT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_ROLLOUT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
