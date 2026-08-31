from typing import Literal

ApiV1PricingOrganizationProductsChangePricePartialUpdateObjectIdErrorComponentAttr = Literal["object_id"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsChangePricePartialUpdateObjectIdErrorComponentAttr
] = {
    "object_id",
}


def check_api_v1_pricing_organization_products_change_price_partial_update_object_id_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsChangePricePartialUpdateObjectIdErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
