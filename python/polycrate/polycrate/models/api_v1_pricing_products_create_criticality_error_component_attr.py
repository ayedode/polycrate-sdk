from typing import Literal

ApiV1PricingProductsCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PRICING_PRODUCTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_pricing_products_create_criticality_error_component_attr(
    value: str,
) -> ApiV1PricingProductsCreateCriticalityErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
