from typing import Literal

ApiV1BlockRolloutsUpdateTotalItemsErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_BLOCK_ROLLOUTS_UPDATE_TOTAL_ITEMS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsUpdateTotalItemsErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_block_rollouts_update_total_items_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsUpdateTotalItemsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_TOTAL_ITEMS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_TOTAL_ITEMS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
