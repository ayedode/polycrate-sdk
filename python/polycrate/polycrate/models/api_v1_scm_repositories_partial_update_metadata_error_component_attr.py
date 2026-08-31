from typing import Literal

ApiV1ScmRepositoriesPartialUpdateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesPartialUpdateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_scm_repositories_partial_update_metadata_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesPartialUpdateMetadataErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
