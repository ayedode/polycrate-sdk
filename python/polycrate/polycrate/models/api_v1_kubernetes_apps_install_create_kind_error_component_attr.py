from typing import Literal

ApiV1KubernetesAppsInstallCreateKindErrorComponentAttr = Literal["kind"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_kubernetes_apps_install_create_kind_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateKindErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
