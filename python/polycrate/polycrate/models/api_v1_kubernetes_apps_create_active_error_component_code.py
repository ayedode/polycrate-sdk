from typing import Literal

ApiV1KubernetesAppsCreateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsCreateActiveErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_create_active_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsCreateActiveErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
