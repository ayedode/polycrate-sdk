from typing import Literal

ApiV1ArtifactsUpdateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_ARTIFACTS_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsUpdateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_artifacts_update_actual_availability_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateActualAvailabilityErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
