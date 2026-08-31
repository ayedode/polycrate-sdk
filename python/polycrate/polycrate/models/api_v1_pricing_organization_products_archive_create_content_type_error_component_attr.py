from typing import Literal

ApiV1PricingOrganizationProductsArchiveCreateContentTypeErrorComponentAttr = Literal["content_type"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsArchiveCreateContentTypeErrorComponentAttr
] = {
    "content_type",
}


def check_api_v1_pricing_organization_products_archive_create_content_type_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsArchiveCreateContentTypeErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
