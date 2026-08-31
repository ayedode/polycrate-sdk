from typing import Literal

ApiV1PricingProductsCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_PRODUCTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_products_create_annotations_error_component_code(
    value: str,
) -> ApiV1PricingProductsCreateAnnotationsErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
