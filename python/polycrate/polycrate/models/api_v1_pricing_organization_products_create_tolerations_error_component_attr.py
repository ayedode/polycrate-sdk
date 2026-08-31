from typing import Literal

ApiV1PricingOrganizationProductsCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_pricing_organization_products_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsCreateTolerationsErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
