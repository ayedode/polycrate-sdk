from typing import Literal

ApiV1BlockRolloutItemsPartialUpdateDisplayNameErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsPartialUpdateDisplayNameErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_block_rollout_items_partial_update_display_name_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsPartialUpdateDisplayNameErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
