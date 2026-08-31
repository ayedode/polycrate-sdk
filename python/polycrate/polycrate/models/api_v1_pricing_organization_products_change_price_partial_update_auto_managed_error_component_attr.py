from typing import Literal

ApiV1PricingOrganizationProductsChangePricePartialUpdateAutoManagedErrorComponentAttr = Literal["auto_managed"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_AUTO_MANAGED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsChangePricePartialUpdateAutoManagedErrorComponentAttr
] = {
    "auto_managed",
}


def check_api_v1_pricing_organization_products_change_price_partial_update_auto_managed_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsChangePricePartialUpdateAutoManagedErrorComponentAttr:
    if (
        value
        in API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_AUTO_MANAGED_ERROR_COMPONENT_ATTR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_AUTO_MANAGED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
