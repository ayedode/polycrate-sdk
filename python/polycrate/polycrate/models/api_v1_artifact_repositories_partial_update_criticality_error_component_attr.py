from typing import Literal

ApiV1ArtifactRepositoriesPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_artifact_repositories_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
