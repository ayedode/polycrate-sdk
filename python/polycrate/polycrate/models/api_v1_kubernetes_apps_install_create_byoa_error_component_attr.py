from typing import Literal

ApiV1KubernetesAppsInstallCreateByoaErrorComponentAttr = Literal["byoa"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_BYOA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateByoaErrorComponentAttr
] = {
    "byoa",
}


def check_api_v1_kubernetes_apps_install_create_byoa_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateByoaErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_BYOA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_BYOA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
