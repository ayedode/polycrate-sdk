from typing import Literal

ApiV1PricingProductsReconcileCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsReconcileCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_pricing_products_reconcile_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1PricingProductsReconcileCreateTolerationsErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
