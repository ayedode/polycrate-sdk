from typing import Literal

ApiV1ScmRepositoriesPartialUpdateHostnameErrorComponentAttr = Literal["hostname"]

API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesPartialUpdateHostnameErrorComponentAttr
] = {
    "hostname",
}


def check_api_v1_scm_repositories_partial_update_hostname_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesPartialUpdateHostnameErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
