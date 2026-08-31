from typing import Literal

ApiV1PricingProductsReconcileCreateProviderTypeIdErrorComponentAttr = Literal["provider_type_id"]

API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_PROVIDER_TYPE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsReconcileCreateProviderTypeIdErrorComponentAttr
] = {
    "provider_type_id",
}


def check_api_v1_pricing_products_reconcile_create_provider_type_id_error_component_attr(
    value: str,
) -> ApiV1PricingProductsReconcileCreateProviderTypeIdErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_PROVIDER_TYPE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_PROVIDER_TYPE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
