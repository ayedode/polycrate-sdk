from typing import Literal

ApiV1ArtifactsPartialUpdateReadmeMdErrorComponentAttr = Literal["readme_md"]

API_V1_ARTIFACTS_PARTIAL_UPDATE_README_MD_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsPartialUpdateReadmeMdErrorComponentAttr
] = {
    "readme_md",
}


def check_api_v1_artifacts_partial_update_readme_md_error_component_attr(
    value: str,
) -> ApiV1ArtifactsPartialUpdateReadmeMdErrorComponentAttr:
    if value in API_V1_ARTIFACTS_PARTIAL_UPDATE_README_MD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_PARTIAL_UPDATE_README_MD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
