from typing import Literal

ApiV1ScmRepositoriesCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_SCM_REPOSITORIES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_scm_repositories_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
