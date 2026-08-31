from typing import Literal

ApiV1PopsUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_POPS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsUpdateSlaTargetErrorComponentAttr] = {
    "sla_target",
}


def check_api_v1_pops_update_sla_target_error_component_attr(value: str) -> ApiV1PopsUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_POPS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
