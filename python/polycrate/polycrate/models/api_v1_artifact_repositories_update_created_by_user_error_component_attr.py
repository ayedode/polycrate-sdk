from typing import Literal

ApiV1ArtifactRepositoriesUpdateCreatedByUserErrorComponentAttr = Literal["created_by_user"]

API_V1_ARTIFACT_REPOSITORIES_UPDATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesUpdateCreatedByUserErrorComponentAttr
] = {
    "created_by_user",
}


def check_api_v1_artifact_repositories_update_created_by_user_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesUpdateCreatedByUserErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_UPDATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_UPDATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
