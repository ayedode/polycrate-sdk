from typing import Literal

ApiV1KubernetesVolumesCreateProviderObjectIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_VOLUMES_CREATE_PROVIDER_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesCreateProviderObjectIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_volumes_create_provider_object_id_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesCreateProviderObjectIdErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_PROVIDER_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_PROVIDER_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
