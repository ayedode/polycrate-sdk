from typing import Literal

ApiV1KubernetesAddonsUpdateNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_ADDONS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_kubernetes_addons_update_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsUpdateNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
