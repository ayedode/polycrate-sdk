from typing import Literal

ApiV1ArtifactRepositoriesUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_ARTIFACT_REPOSITORIES_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_artifact_repositories_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
