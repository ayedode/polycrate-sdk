from typing import Literal

ApiV1KubernetesAppsPartialUpdatePodsAvailableErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_PODS_AVAILABLE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsPartialUpdatePodsAvailableErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_kubernetes_apps_partial_update_pods_available_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdatePodsAvailableErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_PODS_AVAILABLE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_PODS_AVAILABLE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
