from typing import Literal

ApiV1KubernetesAddonsUpdateAllowMultipleErrorComponentAttr = Literal["allow_multiple"]

API_V1_KUBERNETES_ADDONS_UPDATE_ALLOW_MULTIPLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsUpdateAllowMultipleErrorComponentAttr
] = {
    "allow_multiple",
}


def check_api_v1_kubernetes_addons_update_allow_multiple_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsUpdateAllowMultipleErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_ALLOW_MULTIPLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_ALLOW_MULTIPLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
