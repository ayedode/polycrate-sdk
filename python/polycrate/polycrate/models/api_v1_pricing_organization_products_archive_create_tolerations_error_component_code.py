from typing import Literal

ApiV1PricingOrganizationProductsArchiveCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsArchiveCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_organization_products_archive_create_tolerations_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsArchiveCreateTolerationsErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
