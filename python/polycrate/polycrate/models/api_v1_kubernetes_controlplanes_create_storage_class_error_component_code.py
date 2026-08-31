from typing import Literal

ApiV1KubernetesControlplanesCreateStorageClassErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_STORAGE_CLASS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesCreateStorageClassErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_controlplanes_create_storage_class_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesCreateStorageClassErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_STORAGE_CLASS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_STORAGE_CLASS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
