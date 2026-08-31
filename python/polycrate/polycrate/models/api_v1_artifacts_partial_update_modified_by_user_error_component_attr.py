from typing import Literal

ApiV1ArtifactsPartialUpdateModifiedByUserErrorComponentAttr = Literal["modified_by_user"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsPartialUpdateModifiedByUserErrorComponentAttr
] = {
    "modified_by_user",
}


def check_api_v1_artifacts_partial_update_modified_by_user_error_component_attr(
    value: str,
) -> ApiV1ArtifactsPartialUpdateModifiedByUserErrorComponentAttr:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
