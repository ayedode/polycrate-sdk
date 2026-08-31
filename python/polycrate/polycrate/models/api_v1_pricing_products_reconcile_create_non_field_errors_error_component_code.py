from typing import Literal

ApiV1PricingProductsReconcileCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsReconcileCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_products_reconcile_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1PricingProductsReconcileCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_RECONCILE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
