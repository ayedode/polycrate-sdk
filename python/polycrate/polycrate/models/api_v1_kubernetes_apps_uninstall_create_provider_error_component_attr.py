from typing import Literal

ApiV1KubernetesAppsUninstallCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_kubernetes_apps_uninstall_create_provider_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateProviderErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
