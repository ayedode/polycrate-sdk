from typing import Literal

ApiV1KubernetesAppsReconcileCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_kubernetes_apps_reconcile_create_display_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateDisplayNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
