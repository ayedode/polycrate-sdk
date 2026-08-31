from typing import Literal

ApiV1KubernetesControlplanesPartialUpdateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesPartialUpdateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_kubernetes_controlplanes_partial_update_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesPartialUpdateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
