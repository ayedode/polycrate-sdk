from typing import Literal

ApiV1PricingOrganizationProductsListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsListStateErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_organization_products_list_state_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsListStateErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
