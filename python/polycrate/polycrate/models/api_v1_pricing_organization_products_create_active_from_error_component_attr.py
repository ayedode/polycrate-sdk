from typing import Literal

ApiV1PricingOrganizationProductsCreateActiveFromErrorComponentAttr = Literal["active_from"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_ACTIVE_FROM_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsCreateActiveFromErrorComponentAttr
] = {
    "active_from",
}


def check_api_v1_pricing_organization_products_create_active_from_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsCreateActiveFromErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_ACTIVE_FROM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_ACTIVE_FROM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
