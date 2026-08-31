from typing import Literal

ApiV1OrganizationsArchiveCreateCachedProductCostUpdatedAtErrorComponentAttr = Literal["cached_product_cost_updated_at"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_PRODUCT_COST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateCachedProductCostUpdatedAtErrorComponentAttr
] = {
    "cached_product_cost_updated_at",
}


def check_api_v1_organizations_archive_create_cached_product_cost_updated_at_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateCachedProductCostUpdatedAtErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_PRODUCT_COST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_PRODUCT_COST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
