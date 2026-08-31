from typing import Literal

ApiV1ConditionsUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_CONDITIONS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_conditions_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1ConditionsUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_CONDITIONS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
