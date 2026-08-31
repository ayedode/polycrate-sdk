from typing import Literal

ApiV1AlertsUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_ALERTS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsUpdateSlaTargetErrorComponentAttr] = {
    "sla_target",
}


def check_api_v1_alerts_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1AlertsUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
