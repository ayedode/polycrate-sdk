from typing import Literal

ApiV1ArtifactsCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_ARTIFACTS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_artifacts_create_description_error_component_attr(
    value: str,
) -> ApiV1ArtifactsCreateDescriptionErrorComponentAttr:
    if value in API_V1_ARTIFACTS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
