from typing import Literal

ApiV1KubernetesAppsCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_APPS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_apps_create_provider_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsCreateProviderErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
