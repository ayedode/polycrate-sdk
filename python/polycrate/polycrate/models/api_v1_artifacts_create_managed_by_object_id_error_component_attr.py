from typing import Literal

ApiV1ArtifactsCreateManagedByObjectIdErrorComponentAttr = Literal["managed_by_object_id"]

API_V1_ARTIFACTS_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsCreateManagedByObjectIdErrorComponentAttr
] = {
    "managed_by_object_id",
}


def check_api_v1_artifacts_create_managed_by_object_id_error_component_attr(
    value: str,
) -> ApiV1ArtifactsCreateManagedByObjectIdErrorComponentAttr:
    if value in API_V1_ARTIFACTS_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
