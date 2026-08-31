from typing import Literal

ApiV1PricingProductsCreateBillingIntervalErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_PRODUCTS_CREATE_BILLING_INTERVAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsCreateBillingIntervalErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_products_create_billing_interval_error_component_code(
    value: str,
) -> ApiV1PricingProductsCreateBillingIntervalErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_CREATE_BILLING_INTERVAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_BILLING_INTERVAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
