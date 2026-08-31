from typing import Literal

ApiV1PricingOrganizationProductsCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_pricing_organization_products_create_criticality_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsCreateCriticalityErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
