from typing import Literal

ApiV1BlockRolloutItemsUpdateSourceUserErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_SOURCE_USER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsUpdateSourceUserErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_block_rollout_items_update_source_user_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateSourceUserErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_SOURCE_USER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_SOURCE_USER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
