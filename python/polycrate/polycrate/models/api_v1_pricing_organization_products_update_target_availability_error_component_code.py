from typing import Literal

ApiV1PricingOrganizationProductsUpdateTargetAvailabilityErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsUpdateTargetAvailabilityErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_pricing_organization_products_update_target_availability_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsUpdateTargetAvailabilityErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
