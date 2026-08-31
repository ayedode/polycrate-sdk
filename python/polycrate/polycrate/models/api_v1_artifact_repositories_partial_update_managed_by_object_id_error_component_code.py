from typing import Literal

ApiV1ArtifactRepositoriesPartialUpdateManagedByObjectIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactRepositoriesPartialUpdateManagedByObjectIdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_artifact_repositories_partial_update_managed_by_object_id_error_component_code(
    value: str,
) -> ApiV1ArtifactRepositoriesPartialUpdateManagedByObjectIdErrorComponentCode:
    if value in API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_PARTIAL_UPDATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
