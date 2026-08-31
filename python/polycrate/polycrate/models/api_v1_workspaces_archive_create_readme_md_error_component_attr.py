from typing import Literal

ApiV1WorkspacesArchiveCreateReadmeMdErrorComponentAttr = Literal["readme_md"]

API_V1_WORKSPACES_ARCHIVE_CREATE_README_MD_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesArchiveCreateReadmeMdErrorComponentAttr
] = {
    "readme_md",
}


def check_api_v1_workspaces_archive_create_readme_md_error_component_attr(
    value: str,
) -> ApiV1WorkspacesArchiveCreateReadmeMdErrorComponentAttr:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_README_MD_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_README_MD_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
