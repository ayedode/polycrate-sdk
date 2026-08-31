from typing import Literal

ApiV1KubernetesControlplanesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_KUBERNETES_CONTROLPLANES_LIST_STATE_VALUES: set[ApiV1KubernetesControlplanesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_kubernetes_controlplanes_list_state(value: str) -> ApiV1KubernetesControlplanesListState:
    if value in API_V1_KUBERNETES_CONTROLPLANES_LIST_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_LIST_STATE_VALUES!r}"
    )
