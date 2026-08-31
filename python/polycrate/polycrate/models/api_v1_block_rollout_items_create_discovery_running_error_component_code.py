from typing import Literal

ApiV1BlockRolloutItemsCreateDiscoveryRunningErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_DISCOVERY_RUNNING_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutItemsCreateDiscoveryRunningErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollout_items_create_discovery_running_error_component_code(
    value: str,
) -> ApiV1BlockRolloutItemsCreateDiscoveryRunningErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_DISCOVERY_RUNNING_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_DISCOVERY_RUNNING_ERROR_COMPONENT_CODE_VALUES!r}"
    )
