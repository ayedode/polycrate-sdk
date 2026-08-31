from typing import Literal

ApiV1KubernetesAddonsPartialUpdateAllowMultipleErrorComponentAttr = Literal["allow_multiple"]

API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_ALLOW_MULTIPLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsPartialUpdateAllowMultipleErrorComponentAttr
] = {
    "allow_multiple",
}


def check_api_v1_kubernetes_addons_partial_update_allow_multiple_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsPartialUpdateAllowMultipleErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_ALLOW_MULTIPLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_ALLOW_MULTIPLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
