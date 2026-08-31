from typing import Literal

ApiV1KubernetesAppsInstallCreateBlockErrorComponentAttr = Literal["block"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateBlockErrorComponentAttr
] = {
    "block",
}


def check_api_v1_kubernetes_apps_install_create_block_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateBlockErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
