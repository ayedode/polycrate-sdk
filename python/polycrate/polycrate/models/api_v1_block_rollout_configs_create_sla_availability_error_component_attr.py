from typing import Literal

ApiV1BlockRolloutConfigsCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_block_rollout_configs_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
