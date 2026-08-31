from typing import Literal

ApiV1BlockRolloutItemsCreateStatusErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsCreateStatusErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_block_rollout_items_create_status_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsCreateStatusErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
