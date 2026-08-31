from typing import Literal

ApiV1ArtifactRepositoriesUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_ARTIFACT_REPOSITORIES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_artifact_repositories_update_kind_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesUpdateKindErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
