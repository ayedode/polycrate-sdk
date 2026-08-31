from typing import Literal

ApiV1ArtifactRepositoriesPartialUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesPartialUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_artifact_repositories_partial_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesPartialUpdateProviderIdErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
