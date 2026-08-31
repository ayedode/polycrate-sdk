from typing import Literal

ApiV1AlertroutersIngestCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_ALERTROUTERS_INGEST_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersIngestCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_alertrouters_ingest_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1AlertroutersIngestCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
