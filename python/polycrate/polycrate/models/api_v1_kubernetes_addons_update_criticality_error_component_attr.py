from typing import Literal

ApiV1KubernetesAddonsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_KUBERNETES_ADDONS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_kubernetes_addons_update_criticality_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
