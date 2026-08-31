from typing import Literal

ApiV1KubernetesVolumesListScope = Literal["system", "user"]

API_V1_KUBERNETES_VOLUMES_LIST_SCOPE_VALUES: set[ApiV1KubernetesVolumesListScope] = {
    "system",
    "user",
}


def check_api_v1_kubernetes_volumes_list_scope(value: str) -> ApiV1KubernetesVolumesListScope:
    if value in API_V1_KUBERNETES_VOLUMES_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_LIST_SCOPE_VALUES!r}")
