from typing import Literal

ApiV1KubernetesWorkerPoolsArchiveCreateHardeningEnabledErrorComponentAttr = Literal["hardening_enabled"]

API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_HARDENING_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsArchiveCreateHardeningEnabledErrorComponentAttr
] = {
    "hardening_enabled",
}


def check_api_v1_kubernetes_worker_pools_archive_create_hardening_enabled_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsArchiveCreateHardeningEnabledErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_HARDENING_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_HARDENING_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
