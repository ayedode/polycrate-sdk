from typing import Literal

ApiV1PricingOrganizationProductsListKindErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsListKindErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_organization_products_list_kind_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsListKindErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
