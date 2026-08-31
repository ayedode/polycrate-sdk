from typing import Literal

ApiV1PricingProductsReconcileCreateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsReconcileCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_pricing_products_reconcile_create_name_error_component_attr(
    value: str,
) -> ApiV1PricingProductsReconcileCreateNameErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
