from typing import Literal

ApiV1KubernetesAddonsCreateIsDefaultErrorComponentAttr = Literal["is_default"]

API_V1_KUBERNETES_ADDONS_CREATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsCreateIsDefaultErrorComponentAttr
] = {
    "is_default",
}


def check_api_v1_kubernetes_addons_create_is_default_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsCreateIsDefaultErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_CREATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_CREATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
