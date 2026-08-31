from typing import Literal

ApiV1PricingOrganizationProductsPartialUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsPartialUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_organization_products_partial_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsPartialUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
