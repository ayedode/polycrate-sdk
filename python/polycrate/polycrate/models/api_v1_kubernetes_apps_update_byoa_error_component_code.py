from typing import Literal

ApiV1KubernetesAppsUpdateByoaErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_UPDATE_BYOA_ERROR_COMPONENT_CODE_VALUES: set[ApiV1KubernetesAppsUpdateByoaErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_update_byoa_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsUpdateByoaErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_UPDATE_BYOA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_BYOA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
