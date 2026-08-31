from typing import Literal

ApiV1BlockRolloutsArchiveCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_block_rollouts_archive_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
