from typing import Literal

ApiV1KubernetesVolumesUpdatePvcNameErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_VOLUMES_UPDATE_PVC_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesUpdatePvcNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_volumes_update_pvc_name_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesUpdatePvcNameErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_PVC_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_PVC_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
