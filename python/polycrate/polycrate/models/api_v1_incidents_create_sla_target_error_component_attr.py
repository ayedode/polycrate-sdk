from typing import Literal

ApiV1IncidentsCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_INCIDENTS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IncidentsCreateSlaTargetErrorComponentAttr] = {
    "sla_target",
}


def check_api_v1_incidents_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1IncidentsCreateSlaTargetErrorComponentAttr:
    if value in API_V1_INCIDENTS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
