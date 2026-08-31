from typing import Literal

ApiV1KubernetesAddonsArchiveCreateAllowMultipleErrorComponentAttr = Literal["allow_multiple"]

API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_ALLOW_MULTIPLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsArchiveCreateAllowMultipleErrorComponentAttr
] = {
    "allow_multiple",
}


def check_api_v1_kubernetes_addons_archive_create_allow_multiple_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsArchiveCreateAllowMultipleErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_ALLOW_MULTIPLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_ALLOW_MULTIPLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
