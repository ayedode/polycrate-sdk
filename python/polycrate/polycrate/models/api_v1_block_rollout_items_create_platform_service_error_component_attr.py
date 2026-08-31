from typing import Literal

ApiV1BlockRolloutItemsCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_block_rollout_items_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
