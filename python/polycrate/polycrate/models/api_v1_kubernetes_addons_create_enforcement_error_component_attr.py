from typing import Literal

ApiV1KubernetesAddonsCreateEnforcementErrorComponentAttr = Literal["enforcement"]

API_V1_KUBERNETES_ADDONS_CREATE_ENFORCEMENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsCreateEnforcementErrorComponentAttr
] = {
    "enforcement",
}


def check_api_v1_kubernetes_addons_create_enforcement_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsCreateEnforcementErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_CREATE_ENFORCEMENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_CREATE_ENFORCEMENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
