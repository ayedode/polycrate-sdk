from typing import Literal

ApiV1KubernetesAddonsPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsPartialUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_kubernetes_addons_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsPartialUpdateKindErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
