from typing import Literal

ApiV1PricingOrganizationProductsArchiveCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsArchiveCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_organization_products_archive_create_annotations_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsArchiveCreateAnnotationsErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
