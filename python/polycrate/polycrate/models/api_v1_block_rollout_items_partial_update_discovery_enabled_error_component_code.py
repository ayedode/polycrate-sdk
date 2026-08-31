from typing import Literal

ApiV1BlockRolloutItemsPartialUpdateDiscoveryEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsPartialUpdateDiscoveryEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollout_items_partial_update_discovery_enabled_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsPartialUpdateDiscoveryEnabledErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_PARTIAL_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
