from typing import Literal

ApiV1ArtifactsCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_ARTIFACTS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_artifacts_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1ArtifactsCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_ARTIFACTS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
