from typing import Literal

ApiV1BlockRolloutItemsCreateConditionsErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_CONDITIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsCreateConditionsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollout_items_create_conditions_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsCreateConditionsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_CONDITIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_CONDITIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
