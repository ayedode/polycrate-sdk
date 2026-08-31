from typing import Literal

ApiV1ArtifactRepositoriesUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_ARTIFACT_REPOSITORIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_artifact_repositories_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesUpdateTolerationsErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
