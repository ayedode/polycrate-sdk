from typing import Literal

ApiV1OrganizationsCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_ORGANIZATIONS_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_organizations_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
