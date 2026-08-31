from typing import Literal

ApiV1S3BucketsPolicyUpdatePolicyErrorComponentAttr = Literal["policy"]

API_V1S3_BUCKETS_POLICY_UPDATE_POLICY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsPolicyUpdatePolicyErrorComponentAttr
] = {
    "policy",
}


def check_api_v1s3_buckets_policy_update_policy_error_component_attr(
    value: str,
) -> ApiV1S3BucketsPolicyUpdatePolicyErrorComponentAttr:
    if value in API_V1S3_BUCKETS_POLICY_UPDATE_POLICY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_POLICY_UPDATE_POLICY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
