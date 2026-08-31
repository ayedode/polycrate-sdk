from typing import Literal

ApiV1KubernetesAppsArchiveCreateBlockErrorComponentAttr = Literal["block"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateBlockErrorComponentAttr
] = {
    "block",
}


def check_api_v1_kubernetes_apps_archive_create_block_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateBlockErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
