from typing import Literal

ApiV1OrganizationsReconcileCreateCachedFiringAlertsCountErrorComponentAttr = Literal["cached_firing_alerts_count"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_FIRING_ALERTS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateCachedFiringAlertsCountErrorComponentAttr
] = {
    "cached_firing_alerts_count",
}


def check_api_v1_organizations_reconcile_create_cached_firing_alerts_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateCachedFiringAlertsCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_FIRING_ALERTS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_CACHED_FIRING_ALERTS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
