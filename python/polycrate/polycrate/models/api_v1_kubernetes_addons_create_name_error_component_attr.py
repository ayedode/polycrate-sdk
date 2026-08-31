from typing import Literal

ApiV1KubernetesAddonsCreateNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_ADDONS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_kubernetes_addons_create_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsCreateNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
