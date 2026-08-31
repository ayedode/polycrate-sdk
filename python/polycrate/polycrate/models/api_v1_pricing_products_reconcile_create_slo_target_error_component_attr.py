from typing import Literal

ApiV1PricingProductsReconcileCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsReconcileCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_pricing_products_reconcile_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1PricingProductsReconcileCreateSloTargetErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
