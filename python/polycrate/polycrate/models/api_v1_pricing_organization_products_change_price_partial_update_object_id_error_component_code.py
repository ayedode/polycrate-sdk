from typing import Literal

ApiV1PricingOrganizationProductsChangePricePartialUpdateObjectIdErrorComponentCode = Literal["invalid"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsChangePricePartialUpdateObjectIdErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_organization_products_change_price_partial_update_object_id_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsChangePricePartialUpdateObjectIdErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
