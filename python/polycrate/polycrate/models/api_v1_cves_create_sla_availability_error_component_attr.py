from typing import Literal

ApiV1CvesCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_CVES_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CvesCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_cves_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1CvesCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_CVES_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
