from typing import Literal

ApiV1KubernetesAddonsArchiveCreateBlockNameErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_BLOCK_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsArchiveCreateBlockNameErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_addons_archive_create_block_name_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsArchiveCreateBlockNameErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_BLOCK_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_BLOCK_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
