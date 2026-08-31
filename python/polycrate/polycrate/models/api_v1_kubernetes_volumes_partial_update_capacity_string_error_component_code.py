from typing import Literal

ApiV1KubernetesVolumesPartialUpdateCapacityStringErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_CAPACITY_STRING_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdateCapacityStringErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_volumes_partial_update_capacity_string_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdateCapacityStringErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_CAPACITY_STRING_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_CAPACITY_STRING_ERROR_COMPONENT_CODE_VALUES!r}"
    )
