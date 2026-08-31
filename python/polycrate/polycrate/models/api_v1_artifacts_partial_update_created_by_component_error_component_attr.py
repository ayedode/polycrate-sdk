from typing import Literal

ApiV1ArtifactsPartialUpdateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsPartialUpdateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_artifacts_partial_update_created_by_component_error_component_attr(
    value: str,
) -> ApiV1ArtifactsPartialUpdateCreatedByComponentErrorComponentAttr:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
