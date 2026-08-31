from typing import Literal

ApiV1AlertroutersUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_ALERTROUTERS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_alertrouters_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1AlertroutersUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
