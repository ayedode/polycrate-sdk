from typing import Literal

ApiV1S3ClustersArchiveCreateIncludeInCostStatementErrorComponentAttr = Literal["include_in_cost_statement"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_INCLUDE_IN_COST_STATEMENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersArchiveCreateIncludeInCostStatementErrorComponentAttr
] = {
    "include_in_cost_statement",
}


def check_api_v1s3_clusters_archive_create_include_in_cost_statement_error_component_attr(
    value: str,
) -> ApiV1S3ClustersArchiveCreateIncludeInCostStatementErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_INCLUDE_IN_COST_STATEMENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_INCLUDE_IN_COST_STATEMENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
