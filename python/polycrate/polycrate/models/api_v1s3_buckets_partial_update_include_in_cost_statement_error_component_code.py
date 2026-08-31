from typing import Literal

ApiV1S3BucketsPartialUpdateIncludeInCostStatementErrorComponentCode = Literal["invalid", "null"]

API_V1S3_BUCKETS_PARTIAL_UPDATE_INCLUDE_IN_COST_STATEMENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3BucketsPartialUpdateIncludeInCostStatementErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1s3_buckets_partial_update_include_in_cost_statement_error_component_code(
    value: str,
) -> ApiV1S3BucketsPartialUpdateIncludeInCostStatementErrorComponentCode:
    if value in API_V1S3_BUCKETS_PARTIAL_UPDATE_INCLUDE_IN_COST_STATEMENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_PARTIAL_UPDATE_INCLUDE_IN_COST_STATEMENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
