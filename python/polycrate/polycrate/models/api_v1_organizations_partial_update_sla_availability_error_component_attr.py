from typing import Literal

ApiV1OrganizationsPartialUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_organizations_partial_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
