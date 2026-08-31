from typing import Literal

ApiV1KubernetesWorkerPoolsArchiveCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsArchiveCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_kubernetes_worker_pools_archive_create_display_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsArchiveCreateDisplayNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
