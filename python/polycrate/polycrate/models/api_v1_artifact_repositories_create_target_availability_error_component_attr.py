from typing import Literal

ApiV1ArtifactRepositoriesCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_artifact_repositories_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
