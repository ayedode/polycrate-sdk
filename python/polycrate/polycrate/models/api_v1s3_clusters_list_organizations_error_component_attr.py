from typing import Literal

ApiV1S3ClustersListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1S3_CLUSTERS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1s3_clusters_list_organizations_error_component_attr(
    value: str,
) -> ApiV1S3ClustersListOrganizationsErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
