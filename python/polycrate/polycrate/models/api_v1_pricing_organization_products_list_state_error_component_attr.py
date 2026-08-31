from typing import Literal

ApiV1PricingOrganizationProductsListStateErrorComponentAttr = Literal["state"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_pricing_organization_products_list_state_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsListStateErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
