from typing import Literal

ApiV1KubernetesControlplanesCreatePersistenceSizeErrorComponentCode = Literal[
    "blank", "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_PERSISTENCE_SIZE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesCreatePersistenceSizeErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_controlplanes_create_persistence_size_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesCreatePersistenceSizeErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_PERSISTENCE_SIZE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_PERSISTENCE_SIZE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
