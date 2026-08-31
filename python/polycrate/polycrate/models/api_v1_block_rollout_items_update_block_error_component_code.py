from typing import Literal

ApiV1BlockRolloutItemsUpdateBlockErrorComponentCode = Literal["does_not_exist", "incorrect_type", "null", "required"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_BLOCK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsUpdateBlockErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_block_rollout_items_update_block_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateBlockErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_BLOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_BLOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
