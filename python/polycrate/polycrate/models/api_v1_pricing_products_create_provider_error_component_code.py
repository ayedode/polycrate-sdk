from typing import Literal

ApiV1PricingProductsCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_PRODUCTS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_products_create_provider_error_component_code(
    value: str,
) -> ApiV1PricingProductsCreateProviderErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
