from typing import Literal

ApiV1KubernetesAddonsListEnforcementErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_KUBERNETES_ADDONS_LIST_ENFORCEMENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsListEnforcementErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_kubernetes_addons_list_enforcement_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsListEnforcementErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_LIST_ENFORCEMENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_ENFORCEMENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
