from typing import Literal

ApiV1KubernetesAppsCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_APPS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_apps_create_labels_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsCreateLabelsErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
