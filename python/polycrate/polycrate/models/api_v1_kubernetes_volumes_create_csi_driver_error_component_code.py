from typing import Literal

ApiV1KubernetesVolumesCreateCsiDriverErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_VOLUMES_CREATE_CSI_DRIVER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesCreateCsiDriverErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_volumes_create_csi_driver_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesCreateCsiDriverErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_CSI_DRIVER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_CSI_DRIVER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
