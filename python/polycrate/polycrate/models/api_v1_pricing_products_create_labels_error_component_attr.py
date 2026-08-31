from typing import Literal

ApiV1PricingProductsCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PRICING_PRODUCTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_pricing_products_create_labels_error_component_attr(
    value: str,
) -> ApiV1PricingProductsCreateLabelsErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
