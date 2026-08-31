from typing import Literal

ApiV1BlockRolloutItemsCreateRolloutErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_ROLLOUT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsCreateRolloutErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_block_rollout_items_create_rollout_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsCreateRolloutErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_ROLLOUT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_ROLLOUT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
