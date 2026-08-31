from typing import Literal

ApiV1KubernetesAppsUninstallCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_kubernetes_apps_uninstall_create_annotations_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateAnnotationsErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
