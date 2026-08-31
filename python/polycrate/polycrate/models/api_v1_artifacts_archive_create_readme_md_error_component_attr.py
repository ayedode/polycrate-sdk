from typing import Literal

ApiV1ArtifactsArchiveCreateReadmeMdErrorComponentAttr = Literal["readme_md"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_README_MD_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsArchiveCreateReadmeMdErrorComponentAttr
] = {
    "readme_md",
}


def check_api_v1_artifacts_archive_create_readme_md_error_component_attr(
    value: str,
) -> ApiV1ArtifactsArchiveCreateReadmeMdErrorComponentAttr:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_README_MD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_README_MD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
