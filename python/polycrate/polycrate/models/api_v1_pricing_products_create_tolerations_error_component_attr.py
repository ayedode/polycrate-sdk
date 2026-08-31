from typing import Literal

ApiV1PricingProductsCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PRICING_PRODUCTS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_pricing_products_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1PricingProductsCreateTolerationsErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
