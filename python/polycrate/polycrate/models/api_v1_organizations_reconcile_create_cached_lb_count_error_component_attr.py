from typing import Literal

ApiV1OrganizationsReconcileCreateCachedLbCountErrorComponentAttr = Literal["cached_lb_count"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_LB_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateCachedLbCountErrorComponentAttr
] = {
    "cached_lb_count",
}


def check_api_v1_organizations_reconcile_create_cached_lb_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateCachedLbCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_LB_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_LB_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
