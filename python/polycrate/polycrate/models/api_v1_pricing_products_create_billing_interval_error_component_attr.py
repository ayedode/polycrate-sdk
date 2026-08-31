from typing import Literal

ApiV1PricingProductsCreateBillingIntervalErrorComponentAttr = Literal["billing_interval"]

API_V1_PRICING_PRODUCTS_CREATE_BILLING_INTERVAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsCreateBillingIntervalErrorComponentAttr
] = {
    "billing_interval",
}


def check_api_v1_pricing_products_create_billing_interval_error_component_attr(
    value: str,
) -> ApiV1PricingProductsCreateBillingIntervalErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_CREATE_BILLING_INTERVAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_BILLING_INTERVAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
