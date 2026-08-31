from typing import Literal

ApiV1PricingOrganizationProductsArchiveCreateObjectIdErrorComponentAttr = Literal["object_id"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsArchiveCreateObjectIdErrorComponentAttr
] = {
    "object_id",
}


def check_api_v1_pricing_organization_products_archive_create_object_id_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsArchiveCreateObjectIdErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
