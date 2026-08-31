from typing import Literal

ApiV1KubernetesAddonsArchiveCreateIsDefaultErrorComponentAttr = Literal["is_default"]

API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsArchiveCreateIsDefaultErrorComponentAttr
] = {
    "is_default",
}


def check_api_v1_kubernetes_addons_archive_create_is_default_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsArchiveCreateIsDefaultErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
