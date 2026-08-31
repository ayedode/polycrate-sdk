from typing import Literal

ApiV1PricingProductsReconcileCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsReconcileCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_products_reconcile_create_provider_error_component_attr(
    value: str,
) -> ApiV1PricingProductsReconcileCreateProviderErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
