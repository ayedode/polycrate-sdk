from typing import Literal

ApiV1PricingProductsReconcileCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsReconcileCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_pricing_products_reconcile_create_archived_error_component_attr(
    value: str,
) -> ApiV1PricingProductsReconcileCreateArchivedErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
