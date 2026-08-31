from typing import Literal

ApiV1PricingOrganizationProductsCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_pricing_organization_products_create_archived_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsCreateArchivedErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
