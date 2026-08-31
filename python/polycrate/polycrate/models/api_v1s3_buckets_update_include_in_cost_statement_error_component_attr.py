from typing import Literal

ApiV1S3BucketsUpdateIncludeInCostStatementErrorComponentAttr = Literal["include_in_cost_statement"]

API_V1S3_BUCKETS_UPDATE_INCLUDE_IN_COST_STATEMENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsUpdateIncludeInCostStatementErrorComponentAttr
] = {
    "include_in_cost_statement",
}


def check_api_v1s3_buckets_update_include_in_cost_statement_error_component_attr(
    value: str,
) -> ApiV1S3BucketsUpdateIncludeInCostStatementErrorComponentAttr:
    if value in API_V1S3_BUCKETS_UPDATE_INCLUDE_IN_COST_STATEMENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_UPDATE_INCLUDE_IN_COST_STATEMENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
