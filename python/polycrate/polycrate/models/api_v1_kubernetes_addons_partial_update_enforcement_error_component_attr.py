from typing import Literal

ApiV1KubernetesAddonsPartialUpdateEnforcementErrorComponentAttr = Literal["enforcement"]

API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_ENFORCEMENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsPartialUpdateEnforcementErrorComponentAttr
] = {
    "enforcement",
}


def check_api_v1_kubernetes_addons_partial_update_enforcement_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsPartialUpdateEnforcementErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_ENFORCEMENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_PARTIAL_UPDATE_ENFORCEMENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
