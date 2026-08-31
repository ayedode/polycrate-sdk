from typing import Literal

ApiV1KubernetesAppsReconcileCreateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1_KUBERNETES_APPS_RECONCILE_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsReconcileCreateArchivedByErrorComponentAttr
] = {
    "archived_by",
}


def check_api_v1_kubernetes_apps_reconcile_create_archived_by_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsReconcileCreateArchivedByErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_RECONCILE_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_RECONCILE_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
