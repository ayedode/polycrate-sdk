from typing import Literal

ApiV1PoliciesDryRunCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_POLICIES_DRY_RUN_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_policies_dry_run_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
