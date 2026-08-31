from typing import Literal

ApiV1KubernetesVolumesCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_VOLUMES_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_kubernetes_volumes_create_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesCreateScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
