from typing import Literal

ApiV1PricingOrganizationProductsPartialUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsPartialUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_pricing_organization_products_partial_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsPartialUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
