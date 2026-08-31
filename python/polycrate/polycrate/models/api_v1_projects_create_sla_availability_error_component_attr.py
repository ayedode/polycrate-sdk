from typing import Literal

ApiV1ProjectsCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_PROJECTS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_projects_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1ProjectsCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_PROJECTS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
