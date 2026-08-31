from typing import Literal

ApiV1KubernetesAddonsPartialUpdateIsDefaultErrorComponentAttr = Literal["is_default"]

API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsPartialUpdateIsDefaultErrorComponentAttr
] = {
    "is_default",
}


def check_api_v1_kubernetes_addons_partial_update_is_default_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsPartialUpdateIsDefaultErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
