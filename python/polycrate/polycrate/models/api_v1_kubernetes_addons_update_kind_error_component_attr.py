from typing import Literal

ApiV1KubernetesAddonsUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_KUBERNETES_ADDONS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_kubernetes_addons_update_kind_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsUpdateKindErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
