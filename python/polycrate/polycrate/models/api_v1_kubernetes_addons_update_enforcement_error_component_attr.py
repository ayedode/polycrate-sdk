from typing import Literal

ApiV1KubernetesAddonsUpdateEnforcementErrorComponentAttr = Literal["enforcement"]

API_V1_KUBERNETES_ADDONS_UPDATE_ENFORCEMENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsUpdateEnforcementErrorComponentAttr
] = {
    "enforcement",
}


def check_api_v1_kubernetes_addons_update_enforcement_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsUpdateEnforcementErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_ENFORCEMENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_ENFORCEMENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
