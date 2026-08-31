from typing import Literal

ApiV1PricingProductsCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_PRICING_PRODUCTS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_pricing_products_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1PricingProductsCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
