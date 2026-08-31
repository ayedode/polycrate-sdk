from typing import Literal

ApiV1KubernetesAppsUninstallCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_kubernetes_apps_uninstall_create_labels_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateLabelsErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
