from typing import Literal

ApiV1PricingOrganizationProductsListScope = Literal["system", "user"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_SCOPE_VALUES: set[ApiV1PricingOrganizationProductsListScope] = {
    "system",
    "user",
}


def check_api_v1_pricing_organization_products_list_scope(value: str) -> ApiV1PricingOrganizationProductsListScope:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_SCOPE_VALUES!r}"
    )
