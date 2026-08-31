from typing import Literal

ApiV1ConditionInstancesPartialUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesPartialUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_condition_instances_partial_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesPartialUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
