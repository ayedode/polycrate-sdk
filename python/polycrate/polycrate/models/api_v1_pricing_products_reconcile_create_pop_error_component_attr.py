from typing import Literal

ApiV1PricingProductsReconcileCreatePopErrorComponentAttr = Literal["pop"]

API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_POP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsReconcileCreatePopErrorComponentAttr
] = {
    "pop",
}


def check_api_v1_pricing_products_reconcile_create_pop_error_component_attr(
    value: str,
) -> ApiV1PricingProductsReconcileCreatePopErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_POP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_POP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
