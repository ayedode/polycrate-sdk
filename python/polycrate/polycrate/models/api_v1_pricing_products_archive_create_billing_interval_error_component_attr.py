from typing import Literal

ApiV1PricingProductsArchiveCreateBillingIntervalErrorComponentAttr = Literal["billing_interval"]

API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_BILLING_INTERVAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsArchiveCreateBillingIntervalErrorComponentAttr
] = {
    "billing_interval",
}


def check_api_v1_pricing_products_archive_create_billing_interval_error_component_attr(
    value: str,
) -> ApiV1PricingProductsArchiveCreateBillingIntervalErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_BILLING_INTERVAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_BILLING_INTERVAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
