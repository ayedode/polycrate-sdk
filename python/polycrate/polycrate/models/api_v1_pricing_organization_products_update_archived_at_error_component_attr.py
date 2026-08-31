from typing import Literal

ApiV1PricingOrganizationProductsUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_pricing_organization_products_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
