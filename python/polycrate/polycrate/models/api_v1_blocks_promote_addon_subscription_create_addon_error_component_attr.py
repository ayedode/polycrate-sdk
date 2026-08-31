from typing import Literal

ApiV1BlocksPromoteAddonSubscriptionCreateAddonErrorComponentAttr = Literal["addon"]

API_V1_BLOCKS_PROMOTE_ADDON_SUBSCRIPTION_CREATE_ADDON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPromoteAddonSubscriptionCreateAddonErrorComponentAttr
] = {
    "addon",
}


def check_api_v1_blocks_promote_addon_subscription_create_addon_error_component_attr(
    value: str,
) -> ApiV1BlocksPromoteAddonSubscriptionCreateAddonErrorComponentAttr:
    if value in API_V1_BLOCKS_PROMOTE_ADDON_SUBSCRIPTION_CREATE_ADDON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PROMOTE_ADDON_SUBSCRIPTION_CREATE_ADDON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
