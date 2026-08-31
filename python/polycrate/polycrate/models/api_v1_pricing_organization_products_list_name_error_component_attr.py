from typing import Literal

ApiV1PricingOrganizationProductsListNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsListNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_pricing_organization_products_list_name_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsListNameErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
