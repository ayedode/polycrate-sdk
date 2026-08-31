from typing import Literal

ApiV1ArtifactRepositoriesListKindErrorComponentAttr = Literal["kind"]

API_V1_ARTIFACT_REPOSITORIES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_artifact_repositories_list_kind_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesListKindErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
