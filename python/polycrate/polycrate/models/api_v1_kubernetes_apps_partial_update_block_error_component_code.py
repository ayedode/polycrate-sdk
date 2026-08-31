from typing import Literal

ApiV1KubernetesAppsPartialUpdateBlockErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_BLOCK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateBlockErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_kubernetes_apps_partial_update_block_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateBlockErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_BLOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_BLOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
