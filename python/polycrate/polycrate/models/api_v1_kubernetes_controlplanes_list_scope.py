from typing import Literal

ApiV1KubernetesControlplanesListScope = Literal["system", "user"]

API_V1_KUBERNETES_CONTROLPLANES_LIST_SCOPE_VALUES: set[ApiV1KubernetesControlplanesListScope] = {
    "system",
    "user",
}


def check_api_v1_kubernetes_controlplanes_list_scope(value: str) -> ApiV1KubernetesControlplanesListScope:
    if value in API_V1_KUBERNETES_CONTROLPLANES_LIST_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_LIST_SCOPE_VALUES!r}"
    )
