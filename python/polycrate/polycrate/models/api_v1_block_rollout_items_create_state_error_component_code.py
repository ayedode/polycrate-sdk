from typing import Literal

ApiV1BlockRolloutItemsCreateStateErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsCreateStateErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_block_rollout_items_create_state_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsCreateStateErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
