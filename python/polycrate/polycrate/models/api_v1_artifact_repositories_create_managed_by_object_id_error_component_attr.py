from typing import Literal

ApiV1ArtifactRepositoriesCreateManagedByObjectIdErrorComponentAttr = Literal["managed_by_object_id"]

API_V1_ARTIFACT_REPOSITORIES_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesCreateManagedByObjectIdErrorComponentAttr
] = {
    "managed_by_object_id",
}


def check_api_v1_artifact_repositories_create_managed_by_object_id_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesCreateManagedByObjectIdErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
