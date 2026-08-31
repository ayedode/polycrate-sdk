from typing import Literal

ApiV1KubernetesAppsArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_kubernetes_apps_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
