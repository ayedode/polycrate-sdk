from typing import Literal

ApiV1PricingProductsArchiveCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsArchiveCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_products_archive_create_labels_error_component_code(
    value: str,
) -> ApiV1PricingProductsArchiveCreateLabelsErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
