from typing import Literal

ApiV1PricingProductsReconcileCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsReconcileCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_pricing_products_reconcile_create_criticality_error_component_attr(
    value: str,
) -> ApiV1PricingProductsReconcileCreateCriticalityErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
