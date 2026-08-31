from typing import Literal

ApiV1KubernetesVolumesArchiveCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesArchiveCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_kubernetes_volumes_archive_create_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesArchiveCreateScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
