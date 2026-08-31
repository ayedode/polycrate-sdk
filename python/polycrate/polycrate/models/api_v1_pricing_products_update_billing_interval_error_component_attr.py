from typing import Literal

ApiV1PricingProductsUpdateBillingIntervalErrorComponentAttr = Literal["billing_interval"]

API_V1_PRICING_PRODUCTS_UPDATE_BILLING_INTERVAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsUpdateBillingIntervalErrorComponentAttr
] = {
    "billing_interval",
}


def check_api_v1_pricing_products_update_billing_interval_error_component_attr(
    value: str,
) -> ApiV1PricingProductsUpdateBillingIntervalErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_UPDATE_BILLING_INTERVAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_UPDATE_BILLING_INTERVAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
