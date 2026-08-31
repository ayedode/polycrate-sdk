from typing import Literal

ApiV1OrganizationsReconcileCreateCachedLogs30DErrorComponentAttr = Literal["cached_logs_30d"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_LOGS_30D_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateCachedLogs30DErrorComponentAttr
] = {
    "cached_logs_30d",
}


def check_api_v1_organizations_reconcile_create_cached_logs_30d_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateCachedLogs30DErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_LOGS_30D_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_LOGS_30D_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
