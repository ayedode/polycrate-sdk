from typing import Literal

ApiV1ScmRepositoriesUpdateNameErrorComponentAttr = Literal["name"]

API_V1_SCM_REPOSITORIES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_scm_repositories_update_name_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesUpdateNameErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
