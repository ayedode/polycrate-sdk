from typing import Literal

ApiV1ArtifactRepositoriesCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_artifact_repositories_create_criticality_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateCriticalityErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
