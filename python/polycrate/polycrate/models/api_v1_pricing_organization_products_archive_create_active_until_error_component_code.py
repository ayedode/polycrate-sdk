from typing import Literal

ApiV1PricingOrganizationProductsArchiveCreateActiveUntilErrorComponentCode = Literal["datetime", "invalid"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_ACTIVE_UNTIL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsArchiveCreateActiveUntilErrorComponentCode
] = {
    "datetime",
    "invalid",
}


def check_api_v1_pricing_organization_products_archive_create_active_until_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsArchiveCreateActiveUntilErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_ACTIVE_UNTIL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_ACTIVE_UNTIL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
