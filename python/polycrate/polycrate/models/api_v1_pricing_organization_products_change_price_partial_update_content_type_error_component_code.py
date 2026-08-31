from typing import Literal

ApiV1PricingOrganizationProductsChangePricePartialUpdateContentTypeErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type"
]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsChangePricePartialUpdateContentTypeErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_pricing_organization_products_change_price_partial_update_content_type_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsChangePricePartialUpdateContentTypeErrorComponentCode:
    if (
        value
        in API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
