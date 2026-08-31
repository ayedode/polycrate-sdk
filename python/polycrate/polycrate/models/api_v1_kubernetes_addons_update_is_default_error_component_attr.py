from typing import Literal

ApiV1KubernetesAddonsUpdateIsDefaultErrorComponentAttr = Literal["is_default"]

API_V1_KUBERNETES_ADDONS_UPDATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsUpdateIsDefaultErrorComponentAttr
] = {
    "is_default",
}


def check_api_v1_kubernetes_addons_update_is_default_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsUpdateIsDefaultErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
