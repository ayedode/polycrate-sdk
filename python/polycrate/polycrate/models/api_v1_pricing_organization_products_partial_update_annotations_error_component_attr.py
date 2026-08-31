from typing import Literal

ApiV1PricingOrganizationProductsPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_pricing_organization_products_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
