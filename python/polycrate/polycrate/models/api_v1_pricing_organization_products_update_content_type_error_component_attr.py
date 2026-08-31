from typing import Literal

ApiV1PricingOrganizationProductsUpdateContentTypeErrorComponentAttr = Literal["content_type"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsUpdateContentTypeErrorComponentAttr
] = {
    "content_type",
}


def check_api_v1_pricing_organization_products_update_content_type_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsUpdateContentTypeErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
