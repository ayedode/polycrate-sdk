from typing import Literal

ApiV1ArtifactsUpdateReadmeMdErrorComponentAttr = Literal["readme_md"]

API_V1_ARTIFACTS_UPDATE_README_MD_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ArtifactsUpdateReadmeMdErrorComponentAttr] = {
    "readme_md",
}


def check_api_v1_artifacts_update_readme_md_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateReadmeMdErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_README_MD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_README_MD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
