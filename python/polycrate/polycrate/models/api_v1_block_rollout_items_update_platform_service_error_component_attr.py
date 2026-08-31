from typing import Literal

ApiV1BlockRolloutItemsUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_block_rollout_items_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
