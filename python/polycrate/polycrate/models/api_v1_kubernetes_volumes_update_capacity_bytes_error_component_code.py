from typing import Literal

ApiV1KubernetesVolumesUpdateCapacityBytesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_KUBERNETES_VOLUMES_UPDATE_CAPACITY_BYTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesUpdateCapacityBytesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_kubernetes_volumes_update_capacity_bytes_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesUpdateCapacityBytesErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_CAPACITY_BYTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_CAPACITY_BYTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
