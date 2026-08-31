from typing import Literal

ApiV1BlockRolloutItemsUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_block_rollout_items_update_provider_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateProviderErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
