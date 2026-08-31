from typing import Literal

ApiV1KubernetesAppsArchiveCreatePodsTotalErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_PODS_TOTAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsArchiveCreatePodsTotalErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_kubernetes_apps_archive_create_pods_total_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreatePodsTotalErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_PODS_TOTAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_PODS_TOTAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
