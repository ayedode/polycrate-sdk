from typing import Literal

ApiV1KubernetesAppsArchiveCreatePodsReadyErrorComponentAttr = Literal["pods_ready"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_PODS_READY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreatePodsReadyErrorComponentAttr
] = {
    "pods_ready",
}


def check_api_v1_kubernetes_apps_archive_create_pods_ready_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreatePodsReadyErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_PODS_READY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_PODS_READY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
