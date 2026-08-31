from typing import Literal

ApiV1OrganizationsReconcileCreateCachedProductCostUpdatedAtErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_PRODUCT_COST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsReconcileCreateCachedProductCostUpdatedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_organizations_reconcile_create_cached_product_cost_updated_at_error_component_code(
    value: str,
) -> ApiV1OrganizationsReconcileCreateCachedProductCostUpdatedAtErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_PRODUCT_COST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_PRODUCT_COST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
