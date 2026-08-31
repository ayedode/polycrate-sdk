from typing import Literal

ApiV1PricingProductsCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_PRODUCTS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_products_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1PricingProductsCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
