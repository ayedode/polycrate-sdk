from typing import Literal

ApiV1PricingOrganizationProductsArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_pricing_organization_products_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
