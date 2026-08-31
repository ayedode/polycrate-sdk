from typing import Literal

ApiV1ProjectsPartialUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_PROJECTS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsPartialUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_projects_partial_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1ProjectsPartialUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
