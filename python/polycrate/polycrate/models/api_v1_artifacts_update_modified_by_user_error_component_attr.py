from typing import Literal

ApiV1ArtifactsUpdateModifiedByUserErrorComponentAttr = Literal["modified_by_user"]

API_V1_ARTIFACTS_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsUpdateModifiedByUserErrorComponentAttr
] = {
    "modified_by_user",
}


def check_api_v1_artifacts_update_modified_by_user_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateModifiedByUserErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
