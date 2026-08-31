from typing import Literal

ApiV1AlertsReconcileCreatePodErrorComponentAttr = Literal["pod"]

API_V1_ALERTS_RECONCILE_CREATE_POD_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsReconcileCreatePodErrorComponentAttr] = {
    "pod",
}


def check_api_v1_alerts_reconcile_create_pod_error_component_attr(
    value: str,
) -> ApiV1AlertsReconcileCreatePodErrorComponentAttr:
    if value in API_V1_ALERTS_RECONCILE_CREATE_POD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_RECONCILE_CREATE_POD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
