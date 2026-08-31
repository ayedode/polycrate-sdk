from typing import Literal

ApiV1BlocksPromoteAddonSubscriptionCreateAddonErrorComponentCode = Literal["invalid", "null", "required"]

API_V1_BLOCKS_PROMOTE_ADDON_SUBSCRIPTION_CREATE_ADDON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksPromoteAddonSubscriptionCreateAddonErrorComponentCode
] = {
    "invalid",
    "null",
    "required",
}


def check_api_v1_blocks_promote_addon_subscription_create_addon_error_component_code(
    value: str,
) -> ApiV1BlocksPromoteAddonSubscriptionCreateAddonErrorComponentCode:
    if value in API_V1_BLOCKS_PROMOTE_ADDON_SUBSCRIPTION_CREATE_ADDON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PROMOTE_ADDON_SUBSCRIPTION_CREATE_ADDON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
