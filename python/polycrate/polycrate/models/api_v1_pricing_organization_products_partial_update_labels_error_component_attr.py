from typing import Literal

ApiV1PricingOrganizationProductsPartialUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsPartialUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_pricing_organization_products_partial_update_labels_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsPartialUpdateLabelsErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
