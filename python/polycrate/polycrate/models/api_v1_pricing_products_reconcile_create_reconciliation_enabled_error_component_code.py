from typing import Literal

ApiV1PricingProductsReconcileCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsReconcileCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_products_reconcile_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1PricingProductsReconcileCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
