from typing import Literal

ApiV1PricingProductsPartialUpdateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsPartialUpdateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_pricing_products_partial_update_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1PricingProductsPartialUpdateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
