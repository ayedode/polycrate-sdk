from typing import Literal

ApiV1S3ClustersPartialUpdateIncludeInCostStatementErrorComponentAttr = Literal["include_in_cost_statement"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_INCLUDE_IN_COST_STATEMENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersPartialUpdateIncludeInCostStatementErrorComponentAttr
] = {
    "include_in_cost_statement",
}


def check_api_v1s3_clusters_partial_update_include_in_cost_statement_error_component_attr(
    value: str,
) -> ApiV1S3ClustersPartialUpdateIncludeInCostStatementErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_INCLUDE_IN_COST_STATEMENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_INCLUDE_IN_COST_STATEMENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
