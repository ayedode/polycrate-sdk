from typing import Literal

ApiV1KubernetesAppsArchiveCreatePodsTotalErrorComponentAttr = Literal["pods_total"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_PODS_TOTAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreatePodsTotalErrorComponentAttr
] = {
    "pods_total",
}


def check_api_v1_kubernetes_apps_archive_create_pods_total_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreatePodsTotalErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_PODS_TOTAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_PODS_TOTAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
