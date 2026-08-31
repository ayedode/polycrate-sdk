from typing import Literal

ApiV1KubernetesAddonsArchiveCreateDiscoveryEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsArchiveCreateDiscoveryEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_addons_archive_create_discovery_enabled_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsArchiveCreateDiscoveryEnabledErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
