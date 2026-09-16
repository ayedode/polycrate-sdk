from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_contacts_list_created_by_users_error_component import (
        ApiV1ContactsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_contacts_list_kind_error_component import ApiV1ContactsListKindErrorComponent
    from ..models.api_v1_contacts_list_name_exact_error_component import ApiV1ContactsListNameExactErrorComponent
    from ..models.api_v1_contacts_list_organizations_error_component import ApiV1ContactsListOrganizationsErrorComponent
    from ..models.api_v1_contacts_list_search_error_component import ApiV1ContactsListSearchErrorComponent
    from ..models.api_v1_contacts_list_state_error_component import ApiV1ContactsListStateErrorComponent
    from ..models.api_v1_contacts_list_state_not_error_component import ApiV1ContactsListStateNotErrorComponent
    from ..models.api_v1_contacts_list_time_range_error_component import ApiV1ContactsListTimeRangeErrorComponent


T = TypeVar("T", bound="ApiV1ContactsListValidationError")


@_attrs_define
class ApiV1ContactsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ContactsListCreatedByUsersErrorComponent | ApiV1ContactsListKindErrorComponent |
            ApiV1ContactsListNameExactErrorComponent | ApiV1ContactsListOrganizationsErrorComponent |
            ApiV1ContactsListSearchErrorComponent | ApiV1ContactsListStateErrorComponent |
            ApiV1ContactsListStateNotErrorComponent | ApiV1ContactsListTimeRangeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ContactsListCreatedByUsersErrorComponent
        | ApiV1ContactsListKindErrorComponent
        | ApiV1ContactsListNameExactErrorComponent
        | ApiV1ContactsListOrganizationsErrorComponent
        | ApiV1ContactsListSearchErrorComponent
        | ApiV1ContactsListStateErrorComponent
        | ApiV1ContactsListStateNotErrorComponent
        | ApiV1ContactsListTimeRangeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_contacts_list_created_by_users_error_component import (
            ApiV1ContactsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_list_kind_error_component import (
            ApiV1ContactsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_list_organizations_error_component import (
            ApiV1ContactsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_list_search_error_component import (
            ApiV1ContactsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_list_state_error_component import (
            ApiV1ContactsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_list_state_not_error_component import (
            ApiV1ContactsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_list_time_range_error_component import (
            ApiV1ContactsListTimeRangeErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ContactsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsListStateNotErrorComponent):
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
        from ..models.api_v1_contacts_list_created_by_users_error_component import (
            ApiV1ContactsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_list_kind_error_component import (
            ApiV1ContactsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_list_name_exact_error_component import (
            ApiV1ContactsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_list_organizations_error_component import (
            ApiV1ContactsListOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_list_search_error_component import (
            ApiV1ContactsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_list_state_error_component import (
            ApiV1ContactsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_list_state_not_error_component import (
            ApiV1ContactsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_list_time_range_error_component import (
            ApiV1ContactsListTimeRangeErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ContactsListCreatedByUsersErrorComponent
                | ApiV1ContactsListKindErrorComponent
                | ApiV1ContactsListNameExactErrorComponent
                | ApiV1ContactsListOrganizationsErrorComponent
                | ApiV1ContactsListSearchErrorComponent
                | ApiV1ContactsListStateErrorComponent
                | ApiV1ContactsListStateNotErrorComponent
                | ApiV1ContactsListTimeRangeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_list_error_type_0 = (
                        ApiV1ContactsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_list_error_type_1 = (
                        ApiV1ContactsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_list_error_type_2 = (
                        ApiV1ContactsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_list_error_type_3 = (
                        ApiV1ContactsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_list_error_type_4 = ApiV1ContactsListKindErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_contacts_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_list_error_type_5 = (
                        ApiV1ContactsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_list_error_type_6 = (
                        ApiV1ContactsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_contacts_list_error_type_7 = (
                    ApiV1ContactsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_contacts_list_error_type_7

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_contacts_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_contacts_list_validation_error.additional_properties = d
        return api_v1_contacts_list_validation_error

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
