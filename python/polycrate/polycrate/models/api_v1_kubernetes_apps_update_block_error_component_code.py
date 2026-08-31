from typing import Literal

ApiV1KubernetesAppsUpdateBlockErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_KUBERNETES_APPS_UPDATE_BLOCK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsUpdateBlockErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_kubernetes_apps_update_block_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsUpdateBlockErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_UPDATE_BLOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_BLOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
