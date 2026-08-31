from typing import Literal

ApiV1KubernetesAddonsArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_kubernetes_addons_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
