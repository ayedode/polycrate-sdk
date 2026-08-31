from typing import Literal

ApiV1PricingOrganizationProductsListKind = Literal["generic"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_KIND_VALUES: set[ApiV1PricingOrganizationProductsListKind] = {
    "generic",
}


def check_api_v1_pricing_organization_products_list_kind(value: str) -> ApiV1PricingOrganizationProductsListKind:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_KIND_VALUES!r}"
    )
