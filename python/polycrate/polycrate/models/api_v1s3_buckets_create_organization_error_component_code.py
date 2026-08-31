from typing import Literal

ApiV1S3BucketsCreateOrganizationErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1S3_BUCKETS_CREATE_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3BucketsCreateOrganizationErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1s3_buckets_create_organization_error_component_code(
    value: str,
) -> ApiV1S3BucketsCreateOrganizationErrorComponentCode:
    if value in API_V1S3_BUCKETS_CREATE_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_CREATE_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
