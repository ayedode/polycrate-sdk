from typing import Literal

ApiV1S3ClustersUpdateIncludeInCostStatementErrorComponentAttr = Literal["include_in_cost_statement"]

API_V1S3_CLUSTERS_UPDATE_INCLUDE_IN_COST_STATEMENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersUpdateIncludeInCostStatementErrorComponentAttr
] = {
    "include_in_cost_statement",
}


def check_api_v1s3_clusters_update_include_in_cost_statement_error_component_attr(
    value: str,
) -> ApiV1S3ClustersUpdateIncludeInCostStatementErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_INCLUDE_IN_COST_STATEMENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_INCLUDE_IN_COST_STATEMENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
