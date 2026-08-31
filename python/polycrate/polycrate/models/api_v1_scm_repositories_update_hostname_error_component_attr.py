from typing import Literal

ApiV1ScmRepositoriesUpdateHostnameErrorComponentAttr = Literal["hostname"]

API_V1_SCM_REPOSITORIES_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesUpdateHostnameErrorComponentAttr
] = {
    "hostname",
}


def check_api_v1_scm_repositories_update_hostname_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesUpdateHostnameErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
