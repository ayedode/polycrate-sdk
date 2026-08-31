from typing import Literal

ApiV1KubernetesVolumesListPhase = Literal["Available", "Bound", "Failed", "Pending", "Released", "Unknown"]

API_V1_KUBERNETES_VOLUMES_LIST_PHASE_VALUES: set[ApiV1KubernetesVolumesListPhase] = {
    "Available",
    "Bound",
    "Failed",
    "Pending",
    "Released",
    "Unknown",
}


def check_api_v1_kubernetes_volumes_list_phase(value: str) -> ApiV1KubernetesVolumesListPhase:
    if value in API_V1_KUBERNETES_VOLUMES_LIST_PHASE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_LIST_PHASE_VALUES!r}")
