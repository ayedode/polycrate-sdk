from typing import Literal

ApiV1PricingProductsArchiveCreateBillingIntervalErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_BILLING_INTERVAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsArchiveCreateBillingIntervalErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_products_archive_create_billing_interval_error_component_code(
    value: str,
) -> ApiV1PricingProductsArchiveCreateBillingIntervalErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_BILLING_INTERVAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_BILLING_INTERVAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
