from typing import Literal

ApiV1AlertsReconcileCreateLastSeenErrorComponentAttr = Literal["last_seen"]

API_V1_ALERTS_RECONCILE_CREATE_LAST_SEEN_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsReconcileCreateLastSeenErrorComponentAttr
] = {
    "last_seen",
}


def check_api_v1_alerts_reconcile_create_last_seen_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreateLastSeenErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_LAST_SEEN_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_LAST_SEEN_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
