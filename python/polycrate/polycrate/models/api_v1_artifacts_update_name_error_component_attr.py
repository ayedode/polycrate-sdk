from typing import Literal

ApiV1ArtifactsUpdateNameErrorComponentAttr = Literal["name"]

API_V1_ARTIFACTS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_artifacts_update_name_error_component_attr(value: str) -> ApiV1ArtifactsUpdateNameErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
