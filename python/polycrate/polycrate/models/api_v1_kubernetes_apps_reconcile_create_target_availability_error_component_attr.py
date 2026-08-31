from typing import Literal

ApiV1KubernetesAppsReconcileCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_kubernetes_apps_reconcile_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
