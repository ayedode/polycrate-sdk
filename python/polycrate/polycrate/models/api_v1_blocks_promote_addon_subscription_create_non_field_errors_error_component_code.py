from typing import Literal

ApiV1BlocksPromoteAddonSubscriptionCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_PROMOTE_ADDON_SUBSCRIPTION_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksPromoteAddonSubscriptionCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_promote_addon_subscription_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1BlocksPromoteAddonSubscriptionCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_BLOCKS_PROMOTE_ADDON_SUBSCRIPTION_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PROMOTE_ADDON_SUBSCRIPTION_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
