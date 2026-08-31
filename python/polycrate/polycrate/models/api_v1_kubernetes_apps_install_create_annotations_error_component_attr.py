from typing import Literal

ApiV1KubernetesAppsInstallCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_kubernetes_apps_install_create_annotations_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateAnnotationsErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
