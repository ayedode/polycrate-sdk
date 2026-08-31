from typing import Literal

ApiV1KubernetesAppsInstallCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsInstallCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_apps_install_create_provider_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateProviderErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
