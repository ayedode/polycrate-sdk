from typing import Literal

ApiV1ScmRepositoriesArchiveCreateHostnameErrorComponentAttr = Literal["hostname"]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreateHostnameErrorComponentAttr
] = {
    "hostname",
}


def check_api_v1_scm_repositories_archive_create_hostname_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreateHostnameErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
