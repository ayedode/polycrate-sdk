from typing import Literal

ApiV1KubernetesAppsUninstallCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_apps_uninstall_create_annotations_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateAnnotationsErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
