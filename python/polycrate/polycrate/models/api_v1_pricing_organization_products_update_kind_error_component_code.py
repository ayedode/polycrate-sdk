from typing import Literal

ApiV1PricingOrganizationProductsUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_organization_products_update_kind_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsUpdateKindErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
