from typing import Literal

ApiV1KubernetesAppsReconcileCreateModifiedByUserErrorComponentAttr = Literal["modified_by_user"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateModifiedByUserErrorComponentAttr
] = {
    "modified_by_user",
}


def check_api_v1_kubernetes_apps_reconcile_create_modified_by_user_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateModifiedByUserErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
