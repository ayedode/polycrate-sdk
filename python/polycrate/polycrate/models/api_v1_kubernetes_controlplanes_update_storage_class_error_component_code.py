from typing import Literal

ApiV1KubernetesControlplanesUpdateStorageClassErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_STORAGE_CLASS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesUpdateStorageClassErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_controlplanes_update_storage_class_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateStorageClassErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_STORAGE_CLASS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_STORAGE_CLASS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
