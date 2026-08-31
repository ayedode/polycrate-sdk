from typing import Literal

ApiV1PricingProductsReconcileCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsReconcileCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_products_reconcile_create_archived_error_component_code(
    value: str,
) -> ApiV1PricingProductsReconcileCreateArchivedErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
