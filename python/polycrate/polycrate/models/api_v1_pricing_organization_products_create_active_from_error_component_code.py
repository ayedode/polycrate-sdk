from typing import Literal

ApiV1PricingOrganizationProductsCreateActiveFromErrorComponentCode = Literal["datetime", "invalid"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_ACTIVE_FROM_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsCreateActiveFromErrorComponentCode
] = {
    "datetime",
    "invalid",
}


def check_api_v1_pricing_organization_products_create_active_from_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsCreateActiveFromErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_ACTIVE_FROM_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_ACTIVE_FROM_ERROR_COMPONENT_CODE_VALUES!r}"
    )
