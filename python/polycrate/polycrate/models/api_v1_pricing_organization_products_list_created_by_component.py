from typing import Literal

ApiV1PricingOrganizationProductsListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_CREATED_BY_COMPONENT_VALUES: set[
    ApiV1PricingOrganizationProductsListCreatedByComponent
] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_pricing_organization_products_list_created_by_component(
    value: str,
) -> ApiV1PricingOrganizationProductsListCreatedByComponent:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
