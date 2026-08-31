from typing import Literal

ApiV1KubernetesControlplanesUpdatePersistenceSizeErrorComponentAttr = Literal["persistence_size"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_PERSISTENCE_SIZE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesUpdatePersistenceSizeErrorComponentAttr
] = {
    "persistence_size",
}


def check_api_v1_kubernetes_controlplanes_update_persistence_size_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesUpdatePersistenceSizeErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_PERSISTENCE_SIZE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_PERSISTENCE_SIZE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
