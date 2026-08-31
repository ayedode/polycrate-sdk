from typing import Literal

ApiV1PricingOrganizationProductsChangePricePartialUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsChangePricePartialUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_organization_products_change_price_partial_update_labels_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsChangePricePartialUpdateLabelsErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
