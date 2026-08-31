from typing import Literal

ApiV1KubernetesControlplanesArchiveCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesArchiveCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_kubernetes_controlplanes_archive_create_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesArchiveCreateScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
