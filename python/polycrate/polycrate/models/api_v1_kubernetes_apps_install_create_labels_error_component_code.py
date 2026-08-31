from typing import Literal

ApiV1KubernetesAppsInstallCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsInstallCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_apps_install_create_labels_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateLabelsErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
