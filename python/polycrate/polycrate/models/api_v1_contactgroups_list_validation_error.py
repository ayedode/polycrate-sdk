from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_contactgroups_list_contacts_error_component import ApiV1ContactgroupsListContactsErrorComponent
    from ..models.api_v1_contactgroups_list_created_by_users_error_component import (
        ApiV1ContactgroupsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_contactgroups_list_identity_providers_error_component import (
        ApiV1ContactgroupsListIdentityProvidersErrorComponent,
    )
    from ..models.api_v1_contactgroups_list_kind_error_component import ApiV1ContactgroupsListKindErrorComponent
    from ..models.api_v1_contactgroups_list_name_exact_error_component import (
        ApiV1ContactgroupsListNameExactErrorComponent,
    )
    from ..models.api_v1_contactgroups_list_organizations_error_component import (
        ApiV1ContactgroupsListOrganizationsErrorComponent,
    )
    from ..models.api_v1_contactgroups_list_search_error_component import ApiV1ContactgroupsListSearchErrorComponent
    from ..models.api_v1_contactgroups_list_state_error_component import ApiV1ContactgroupsListStateErrorComponent
    from ..models.api_v1_contactgroups_list_state_not_error_component import (
        ApiV1ContactgroupsListStateNotErrorComponent,
    )
    from ..models.api_v1_contactgroups_list_time_range_error_component import (
        ApiV1ContactgroupsListTimeRangeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ContactgroupsListValidationError")


@_attrs_define
class ApiV1ContactgroupsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ContactgroupsListContactsErrorComponent | ApiV1ContactgroupsListCreatedByUsersErrorComponent |
            ApiV1ContactgroupsListIdentityProvidersErrorComponent | ApiV1ContactgroupsListKindErrorComponent |
            ApiV1ContactgroupsListNameExactErrorComponent | ApiV1ContactgroupsListOrganizationsErrorComponent |
            ApiV1ContactgroupsListSearchErrorComponent | ApiV1ContactgroupsListStateErrorComponent |
            ApiV1ContactgroupsListStateNotErrorComponent | ApiV1ContactgroupsListTimeRangeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ContactgroupsListContactsErrorComponent
        | ApiV1ContactgroupsListCreatedByUsersErrorComponent
        | ApiV1ContactgroupsListIdentityProvidersErrorComponent
        | ApiV1ContactgroupsListKindErrorComponent
        | ApiV1ContactgroupsListNameExactErrorComponent
        | ApiV1ContactgroupsListOrganizationsErrorComponent
        | ApiV1ContactgroupsListSearchErrorComponent
        | ApiV1ContactgroupsListStateErrorComponent
        | ApiV1ContactgroupsListStateNotErrorComponent
        | ApiV1ContactgroupsListTimeRangeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_contactgroups_list_contacts_error_component import (
            ApiV1ContactgroupsListContactsErrorComponent,
        )
        from ..models.api_v1_contactgroups_list_created_by_users_error_component import (
            ApiV1ContactgroupsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_contactgroups_list_identity_providers_error_component import (
            ApiV1ContactgroupsListIdentityProvidersErrorComponent,
        )
        from ..models.api_v1_contactgroups_list_kind_error_component import ApiV1ContactgroupsListKindErrorComponent
        from ..models.api_v1_contactgroups_list_organizations_error_component import (
            ApiV1ContactgroupsListOrganizationsErrorComponent,
        )
        from ..models.api_v1_contactgroups_list_search_error_component import ApiV1ContactgroupsListSearchErrorComponent
        from ..models.api_v1_contactgroups_list_state_error_component import ApiV1ContactgroupsListStateErrorComponent
        from ..models.api_v1_contactgroups_list_state_not_error_component import (
            ApiV1ContactgroupsListStateNotErrorComponent,
        )
        from ..models.api_v1_contactgroups_list_time_range_error_component import (
            ApiV1ContactgroupsListTimeRangeErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ContactgroupsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactgroupsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactgroupsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactgroupsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactgroupsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactgroupsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactgroupsListContactsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactgroupsListIdentityProvidersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactgroupsListStateNotErrorComponent):
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
        from ..models.api_v1_contactgroups_list_contacts_error_component import (
            ApiV1ContactgroupsListContactsErrorComponent,
        )
        from ..models.api_v1_contactgroups_list_created_by_users_error_component import (
            ApiV1ContactgroupsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_contactgroups_list_identity_providers_error_component import (
            ApiV1ContactgroupsListIdentityProvidersErrorComponent,
        )
        from ..models.api_v1_contactgroups_list_kind_error_component import ApiV1ContactgroupsListKindErrorComponent
        from ..models.api_v1_contactgroups_list_name_exact_error_component import (
            ApiV1ContactgroupsListNameExactErrorComponent,
        )
        from ..models.api_v1_contactgroups_list_organizations_error_component import (
            ApiV1ContactgroupsListOrganizationsErrorComponent,
        )
        from ..models.api_v1_contactgroups_list_search_error_component import ApiV1ContactgroupsListSearchErrorComponent
        from ..models.api_v1_contactgroups_list_state_error_component import ApiV1ContactgroupsListStateErrorComponent
        from ..models.api_v1_contactgroups_list_state_not_error_component import (
            ApiV1ContactgroupsListStateNotErrorComponent,
        )
        from ..models.api_v1_contactgroups_list_time_range_error_component import (
            ApiV1ContactgroupsListTimeRangeErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ContactgroupsListContactsErrorComponent
                | ApiV1ContactgroupsListCreatedByUsersErrorComponent
                | ApiV1ContactgroupsListIdentityProvidersErrorComponent
                | ApiV1ContactgroupsListKindErrorComponent
                | ApiV1ContactgroupsListNameExactErrorComponent
                | ApiV1ContactgroupsListOrganizationsErrorComponent
                | ApiV1ContactgroupsListSearchErrorComponent
                | ApiV1ContactgroupsListStateErrorComponent
                | ApiV1ContactgroupsListStateNotErrorComponent
                | ApiV1ContactgroupsListTimeRangeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contactgroups_list_error_type_0 = (
                        ApiV1ContactgroupsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contactgroups_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contactgroups_list_error_type_1 = (
                        ApiV1ContactgroupsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contactgroups_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contactgroups_list_error_type_2 = (
                        ApiV1ContactgroupsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contactgroups_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contactgroups_list_error_type_3 = (
                        ApiV1ContactgroupsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contactgroups_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contactgroups_list_error_type_4 = (
                        ApiV1ContactgroupsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contactgroups_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contactgroups_list_error_type_5 = (
                        ApiV1ContactgroupsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contactgroups_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contactgroups_list_error_type_6 = (
                        ApiV1ContactgroupsListContactsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contactgroups_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contactgroups_list_error_type_7 = (
                        ApiV1ContactgroupsListIdentityProvidersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contactgroups_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contactgroups_list_error_type_8 = (
                        ApiV1ContactgroupsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contactgroups_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_contactgroups_list_error_type_9 = (
                    ApiV1ContactgroupsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_contactgroups_list_error_type_9

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_contactgroups_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_contactgroups_list_validation_error.additional_properties = d
        return api_v1_contactgroups_list_validation_error

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
