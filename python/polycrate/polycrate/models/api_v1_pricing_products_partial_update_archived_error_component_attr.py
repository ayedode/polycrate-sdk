from typing import Literal

ApiV1PricingProductsPartialUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsPartialUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_pricing_products_partial_update_archived_error_component_attr(
    value: str,
) -> ApiV1PricingProductsPartialUpdateArchivedErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
