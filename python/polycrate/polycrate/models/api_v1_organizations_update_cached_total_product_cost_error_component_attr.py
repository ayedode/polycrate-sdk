from typing import Literal

ApiV1OrganizationsUpdateCachedTotalProductCostErrorComponentAttr = Literal["cached_total_product_cost"]

API_V1_ORGANIZATIONS_UPDATE_CACHED_TOTAL_PRODUCT_COST_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateCachedTotalProductCostErrorComponentAttr
] = {
    "cached_total_product_cost",
}


def check_api_v1_organizations_update_cached_total_product_cost_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateCachedTotalProductCostErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_CACHED_TOTAL_PRODUCT_COST_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_CACHED_TOTAL_PRODUCT_COST_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
