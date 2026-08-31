from typing import Literal

ApiV1AlertroutersIngestCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_ALERTROUTERS_INGEST_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersIngestCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_alertrouters_ingest_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1AlertroutersIngestCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
