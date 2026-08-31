from typing import Literal

ApiV1CvesCreateCreatedByUserErrorComponentAttr = Literal["created_by_user"]

API_V1_CVES_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesCreateCreatedByUserErrorComponentAttr] = {
    "created_by_user",
}


def check_api_v1_cves_create_created_by_user_error_component_attr(
    value: str,
) -> ApiV1CvesCreateCreatedByUserErrorComponentAttr:
    if value in API_V1_CVES_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
