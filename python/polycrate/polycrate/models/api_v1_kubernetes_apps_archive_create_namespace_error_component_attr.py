from typing import Literal

ApiV1KubernetesAppsArchiveCreateNamespaceErrorComponentAttr = Literal["namespace"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateNamespaceErrorComponentAttr
] = {
    "namespace",
}


def check_api_v1_kubernetes_apps_archive_create_namespace_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateNamespaceErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
