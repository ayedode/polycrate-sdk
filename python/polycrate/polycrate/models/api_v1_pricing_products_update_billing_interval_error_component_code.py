from typing import Literal

ApiV1PricingProductsUpdateBillingIntervalErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_PRODUCTS_UPDATE_BILLING_INTERVAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsUpdateBillingIntervalErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_products_update_billing_interval_error_component_code(
    value: str,
) -> ApiV1PricingProductsUpdateBillingIntervalErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_UPDATE_BILLING_INTERVAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_UPDATE_BILLING_INTERVAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
