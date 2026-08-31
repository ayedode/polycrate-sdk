from typing import Literal

ApiV1PricingOrganizationProductsChangePricePartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsChangePricePartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_pricing_organization_products_change_price_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsChangePricePartialUpdateNameErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
