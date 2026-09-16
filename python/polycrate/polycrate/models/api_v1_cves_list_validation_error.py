from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_cves_list_created_by_users_error_component import ApiV1CvesListCreatedByUsersErrorComponent
    from ..models.api_v1_cves_list_cve_id_error_component import ApiV1CvesListCveIdErrorComponent
    from ..models.api_v1_cves_list_kind_error_component import ApiV1CvesListKindErrorComponent
    from ..models.api_v1_cves_list_name_exact_error_component import ApiV1CvesListNameExactErrorComponent
    from ..models.api_v1_cves_list_search_error_component import ApiV1CvesListSearchErrorComponent
    from ..models.api_v1_cves_list_severity_error_component import ApiV1CvesListSeverityErrorComponent
    from ..models.api_v1_cves_list_state_error_component import ApiV1CvesListStateErrorComponent
    from ..models.api_v1_cves_list_state_not_error_component import ApiV1CvesListStateNotErrorComponent
    from ..models.api_v1_cves_list_status_error_component import ApiV1CvesListStatusErrorComponent
    from ..models.api_v1_cves_list_time_range_error_component import ApiV1CvesListTimeRangeErrorComponent


T = TypeVar("T", bound="ApiV1CvesListValidationError")


@_attrs_define
class ApiV1CvesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CvesListCreatedByUsersErrorComponent | ApiV1CvesListCveIdErrorComponent |
            ApiV1CvesListKindErrorComponent | ApiV1CvesListNameExactErrorComponent | ApiV1CvesListSearchErrorComponent |
            ApiV1CvesListSeverityErrorComponent | ApiV1CvesListStateErrorComponent | ApiV1CvesListStateNotErrorComponent |
            ApiV1CvesListStatusErrorComponent | ApiV1CvesListTimeRangeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CvesListCreatedByUsersErrorComponent
        | ApiV1CvesListCveIdErrorComponent
        | ApiV1CvesListKindErrorComponent
        | ApiV1CvesListNameExactErrorComponent
        | ApiV1CvesListSearchErrorComponent
        | ApiV1CvesListSeverityErrorComponent
        | ApiV1CvesListStateErrorComponent
        | ApiV1CvesListStateNotErrorComponent
        | ApiV1CvesListStatusErrorComponent
        | ApiV1CvesListTimeRangeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_cves_list_created_by_users_error_component import (
            ApiV1CvesListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_list_cve_id_error_component import ApiV1CvesListCveIdErrorComponent  # noqa: PLC0415
        from ..models.api_v1_cves_list_kind_error_component import ApiV1CvesListKindErrorComponent  # noqa: PLC0415
        from ..models.api_v1_cves_list_search_error_component import ApiV1CvesListSearchErrorComponent  # noqa: PLC0415
        from ..models.api_v1_cves_list_severity_error_component import (
            ApiV1CvesListSeverityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_list_state_error_component import ApiV1CvesListStateErrorComponent  # noqa: PLC0415
        from ..models.api_v1_cves_list_state_not_error_component import (
            ApiV1CvesListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_list_status_error_component import ApiV1CvesListStatusErrorComponent  # noqa: PLC0415
        from ..models.api_v1_cves_list_time_range_error_component import (
            ApiV1CvesListTimeRangeErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CvesListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesListSeverityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesListStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesListCveIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CvesListStateNotErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_cves_list_created_by_users_error_component import (
            ApiV1CvesListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_list_cve_id_error_component import ApiV1CvesListCveIdErrorComponent  # noqa: PLC0415
        from ..models.api_v1_cves_list_kind_error_component import ApiV1CvesListKindErrorComponent  # noqa: PLC0415
        from ..models.api_v1_cves_list_name_exact_error_component import (
            ApiV1CvesListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_list_search_error_component import ApiV1CvesListSearchErrorComponent  # noqa: PLC0415
        from ..models.api_v1_cves_list_severity_error_component import (
            ApiV1CvesListSeverityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_list_state_error_component import ApiV1CvesListStateErrorComponent  # noqa: PLC0415
        from ..models.api_v1_cves_list_state_not_error_component import (
            ApiV1CvesListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cves_list_status_error_component import ApiV1CvesListStatusErrorComponent  # noqa: PLC0415
        from ..models.api_v1_cves_list_time_range_error_component import (
            ApiV1CvesListTimeRangeErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CvesListCreatedByUsersErrorComponent
                | ApiV1CvesListCveIdErrorComponent
                | ApiV1CvesListKindErrorComponent
                | ApiV1CvesListNameExactErrorComponent
                | ApiV1CvesListSearchErrorComponent
                | ApiV1CvesListSeverityErrorComponent
                | ApiV1CvesListStateErrorComponent
                | ApiV1CvesListStateNotErrorComponent
                | ApiV1CvesListStatusErrorComponent
                | ApiV1CvesListTimeRangeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_list_error_type_0 = ApiV1CvesListSearchErrorComponent.from_dict(data)

                    return componentsschemas_api_v1_cves_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_list_error_type_1 = ApiV1CvesListTimeRangeErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_list_error_type_2 = ApiV1CvesListStateErrorComponent.from_dict(data)

                    return componentsschemas_api_v1_cves_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_list_error_type_3 = ApiV1CvesListKindErrorComponent.from_dict(data)

                    return componentsschemas_api_v1_cves_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_list_error_type_4 = (
                        ApiV1CvesListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cves_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_list_error_type_5 = ApiV1CvesListSeverityErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_list_error_type_6 = ApiV1CvesListStatusErrorComponent.from_dict(data)

                    return componentsschemas_api_v1_cves_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_list_error_type_7 = ApiV1CvesListCveIdErrorComponent.from_dict(data)

                    return componentsschemas_api_v1_cves_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cves_list_error_type_8 = ApiV1CvesListStateNotErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_cves_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_cves_list_error_type_9 = ApiV1CvesListNameExactErrorComponent.from_dict(data)

                return componentsschemas_api_v1_cves_list_error_type_9

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_cves_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_cves_list_validation_error.additional_properties = d
        return api_v1_cves_list_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
