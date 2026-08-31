from typing import Literal

ApiV1KubernetesAddonsCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_KUBERNETES_ADDONS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_kubernetes_addons_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsCreateSlaTargetErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
