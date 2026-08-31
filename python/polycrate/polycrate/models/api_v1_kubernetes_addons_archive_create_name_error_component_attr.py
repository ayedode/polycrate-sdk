from typing import Literal

ApiV1KubernetesAddonsArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_kubernetes_addons_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsArchiveCreateNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
