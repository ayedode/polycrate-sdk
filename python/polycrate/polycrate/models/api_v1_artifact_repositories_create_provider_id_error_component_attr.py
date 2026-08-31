from typing import Literal

ApiV1ArtifactRepositoriesCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_artifact_repositories_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateProviderIdErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
