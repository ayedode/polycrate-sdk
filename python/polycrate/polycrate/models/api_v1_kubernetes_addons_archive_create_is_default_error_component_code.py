from typing import Literal

ApiV1KubernetesAddonsArchiveCreateIsDefaultErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_IS_DEFAULT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsArchiveCreateIsDefaultErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_addons_archive_create_is_default_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsArchiveCreateIsDefaultErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_IS_DEFAULT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_IS_DEFAULT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
