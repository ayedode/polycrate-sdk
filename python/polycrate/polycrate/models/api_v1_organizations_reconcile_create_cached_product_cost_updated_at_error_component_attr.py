from typing import Literal

ApiV1OrganizationsReconcileCreateCachedProductCostUpdatedAtErrorComponentAttr = Literal[
    "cached_product_cost_updated_at"
]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_PRODUCT_COST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateCachedProductCostUpdatedAtErrorComponentAttr
] = {
    "cached_product_cost_updated_at",
}


def check_api_v1_organizations_reconcile_create_cached_product_cost_updated_at_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateCachedProductCostUpdatedAtErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_PRODUCT_COST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_PRODUCT_COST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
