from typing import Literal

ApiV1PricingOrganizationProductsUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_pricing_organization_products_update_display_name_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
