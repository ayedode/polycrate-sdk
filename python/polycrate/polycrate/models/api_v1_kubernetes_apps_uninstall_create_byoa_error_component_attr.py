from typing import Literal

ApiV1KubernetesAppsUninstallCreateByoaErrorComponentAttr = Literal["byoa"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_BYOA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateByoaErrorComponentAttr
] = {
    "byoa",
}


def check_api_v1_kubernetes_apps_uninstall_create_byoa_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateByoaErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_BYOA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_BYOA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
