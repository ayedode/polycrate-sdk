from typing import Literal

ApiV1KubernetesAddonsUpdateDefaultVersionErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_ADDONS_UPDATE_DEFAULT_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsUpdateDefaultVersionErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_addons_update_default_version_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsUpdateDefaultVersionErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_DEFAULT_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_DEFAULT_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
