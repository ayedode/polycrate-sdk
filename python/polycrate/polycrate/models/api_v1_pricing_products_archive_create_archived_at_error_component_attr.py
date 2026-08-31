from typing import Literal

ApiV1PricingProductsArchiveCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsArchiveCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_pricing_products_archive_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1PricingProductsArchiveCreateArchivedAtErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
