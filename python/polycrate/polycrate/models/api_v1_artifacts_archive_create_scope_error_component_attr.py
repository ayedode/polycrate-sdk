from typing import Literal

ApiV1ArtifactsArchiveCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsArchiveCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_artifacts_archive_create_scope_error_component_attr(
    value: str,
) -> ApiV1ArtifactsArchiveCreateScopeErrorComponentAttr:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
