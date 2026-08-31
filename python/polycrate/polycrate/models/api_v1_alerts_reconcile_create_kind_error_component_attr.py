from typing import Literal

ApiV1AlertsReconcileCreateKindErrorComponentAttr = Literal["kind"]

API_V1_ALERTS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsReconcileCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_alerts_reconcile_create_kind_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreateKindErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
