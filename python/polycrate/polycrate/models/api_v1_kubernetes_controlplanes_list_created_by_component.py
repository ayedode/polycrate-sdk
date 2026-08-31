from typing import Literal

ApiV1KubernetesControlplanesListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_KUBERNETES_CONTROLPLANES_LIST_CREATED_BY_COMPONENT_VALUES: set[
    ApiV1KubernetesControlplanesListCreatedByComponent
] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_kubernetes_controlplanes_list_created_by_component(
    value: str,
) -> ApiV1KubernetesControlplanesListCreatedByComponent:
    if value in API_V1_KUBERNETES_CONTROLPLANES_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
