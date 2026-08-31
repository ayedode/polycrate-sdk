from typing import Literal

ApiV1OrganizationsReconcileCreateGitlabGroupUrlErrorComponentAttr = Literal["gitlab_group_url"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_GITLAB_GROUP_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsReconcileCreateGitlabGroupUrlErrorComponentAttr
] = {
    "gitlab_group_url",
}


def check_api_v1_organizations_reconcile_create_gitlab_group_url_error_component_attr(
    value: str,
) -> ApiV1OrganizationsReconcileCreateGitlabGroupUrlErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_GITLAB_GROUP_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_GITLAB_GROUP_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
