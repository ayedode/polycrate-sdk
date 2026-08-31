from typing import Literal

ApiV1PricingProductsReconcileCreateProviderEntityErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_PROVIDER_ENTITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsReconcileCreateProviderEntityErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_pricing_products_reconcile_create_provider_entity_error_component_code(
    value: str,
) -> ApiV1PricingProductsReconcileCreateProviderEntityErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_PROVIDER_ENTITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_PROVIDER_ENTITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
