from typing import Literal

ApiV1ArtifactRepositoriesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_artifact_repositories_create_kind_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateKindErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
