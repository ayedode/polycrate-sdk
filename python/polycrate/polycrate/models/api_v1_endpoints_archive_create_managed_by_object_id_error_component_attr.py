from typing import Literal

ApiV1EndpointsArchiveCreateManagedByObjectIdErrorComponentAttr = Literal["managed_by_object_id"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsArchiveCreateManagedByObjectIdErrorComponentAttr
] = {
    "managed_by_object_id",
}


def check_api_v1_endpoints_archive_create_managed_by_object_id_error_component_attr(
    value: str,
) -> ApiV1EndpointsArchiveCreateManagedByObjectIdErrorComponentAttr:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
