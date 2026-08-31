from typing import Literal

ApiV1ArtifactRepositoriesListScopeErrorComponentAttr = Literal["scope"]

API_V1_ARTIFACT_REPOSITORIES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesListScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_artifact_repositories_list_scope_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesListScopeErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
