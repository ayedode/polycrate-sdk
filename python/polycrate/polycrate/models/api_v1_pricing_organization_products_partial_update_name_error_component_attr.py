from typing import Literal

ApiV1PricingOrganizationProductsPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_pricing_organization_products_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsPartialUpdateNameErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
