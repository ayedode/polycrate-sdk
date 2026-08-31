from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_prefixes_list_created_by_users_error_component import (
        ApiV1PrefixesListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_prefixes_list_kind_error_component import ApiV1PrefixesListKindErrorComponent
    from ..models.api_v1_prefixes_list_loadbalancer_region_error_component import (
        ApiV1PrefixesListLoadbalancerRegionErrorComponent,
    )
    from ..models.api_v1_prefixes_list_name_exact_error_component import ApiV1PrefixesListNameExactErrorComponent
    from ..models.api_v1_prefixes_list_organizations_error_component import ApiV1PrefixesListOrganizationsErrorComponent
    from ..models.api_v1_prefixes_list_region_error_component import ApiV1PrefixesListRegionErrorComponent
    from ..models.api_v1_prefixes_list_search_error_component import ApiV1PrefixesListSearchErrorComponent
    from ..models.api_v1_prefixes_list_state_error_component import ApiV1PrefixesListStateErrorComponent
    from ..models.api_v1_prefixes_list_state_not_error_component import ApiV1PrefixesListStateNotErrorComponent
    from ..models.api_v1_prefixes_list_time_range_error_component import ApiV1PrefixesListTimeRangeErrorComponent
    from ..models.api_v1_prefixes_list_workspaces_error_component import ApiV1PrefixesListWorkspacesErrorComponent


T = TypeVar("T", bound="ApiV1PrefixesListValidationError")


@_attrs_define
class ApiV1PrefixesListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PrefixesListCreatedByUsersErrorComponent | ApiV1PrefixesListKindErrorComponent |
            ApiV1PrefixesListLoadbalancerRegionErrorComponent | ApiV1PrefixesListNameExactErrorComponent |
            ApiV1PrefixesListOrganizationsErrorComponent | ApiV1PrefixesListRegionErrorComponent |
            ApiV1PrefixesListSearchErrorComponent | ApiV1PrefixesListStateErrorComponent |
            ApiV1PrefixesListStateNotErrorComponent | ApiV1PrefixesListTimeRangeErrorComponent |
            ApiV1PrefixesListWorkspacesErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PrefixesListCreatedByUsersErrorComponent
        | ApiV1PrefixesListKindErrorComponent
        | ApiV1PrefixesListLoadbalancerRegionErrorComponent
        | ApiV1PrefixesListNameExactErrorComponent
        | ApiV1PrefixesListOrganizationsErrorComponent
        | ApiV1PrefixesListRegionErrorComponent
        | ApiV1PrefixesListSearchErrorComponent
        | ApiV1PrefixesListStateErrorComponent
        | ApiV1PrefixesListStateNotErrorComponent
        | ApiV1PrefixesListTimeRangeErrorComponent
        | ApiV1PrefixesListWorkspacesErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_prefixes_list_created_by_users_error_component import (
            ApiV1PrefixesListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_prefixes_list_kind_error_component import ApiV1PrefixesListKindErrorComponent
        from ..models.api_v1_prefixes_list_loadbalancer_region_error_component import (
            ApiV1PrefixesListLoadbalancerRegionErrorComponent,
        )
        from ..models.api_v1_prefixes_list_name_exact_error_component import ApiV1PrefixesListNameExactErrorComponent
        from ..models.api_v1_prefixes_list_organizations_error_component import (
            ApiV1PrefixesListOrganizationsErrorComponent,
        )
        from ..models.api_v1_prefixes_list_search_error_component import ApiV1PrefixesListSearchErrorComponent
        from ..models.api_v1_prefixes_list_state_error_component import ApiV1PrefixesListStateErrorComponent
        from ..models.api_v1_prefixes_list_state_not_error_component import ApiV1PrefixesListStateNotErrorComponent
        from ..models.api_v1_prefixes_list_time_range_error_component import ApiV1PrefixesListTimeRangeErrorComponent
        from ..models.api_v1_prefixes_list_workspaces_error_component import ApiV1PrefixesListWorkspacesErrorComponent

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PrefixesListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesListWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesListStateNotErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesListNameExactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PrefixesListLoadbalancerRegionErrorComponent):
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
        from ..models.api_v1_prefixes_list_created_by_users_error_component import (
            ApiV1PrefixesListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_prefixes_list_kind_error_component import ApiV1PrefixesListKindErrorComponent
        from ..models.api_v1_prefixes_list_loadbalancer_region_error_component import (
            ApiV1PrefixesListLoadbalancerRegionErrorComponent,
        )
        from ..models.api_v1_prefixes_list_name_exact_error_component import ApiV1PrefixesListNameExactErrorComponent
        from ..models.api_v1_prefixes_list_organizations_error_component import (
            ApiV1PrefixesListOrganizationsErrorComponent,
        )
        from ..models.api_v1_prefixes_list_region_error_component import ApiV1PrefixesListRegionErrorComponent
        from ..models.api_v1_prefixes_list_search_error_component import ApiV1PrefixesListSearchErrorComponent
        from ..models.api_v1_prefixes_list_state_error_component import ApiV1PrefixesListStateErrorComponent
        from ..models.api_v1_prefixes_list_state_not_error_component import ApiV1PrefixesListStateNotErrorComponent
        from ..models.api_v1_prefixes_list_time_range_error_component import ApiV1PrefixesListTimeRangeErrorComponent
        from ..models.api_v1_prefixes_list_workspaces_error_component import ApiV1PrefixesListWorkspacesErrorComponent

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PrefixesListCreatedByUsersErrorComponent
                | ApiV1PrefixesListKindErrorComponent
                | ApiV1PrefixesListLoadbalancerRegionErrorComponent
                | ApiV1PrefixesListNameExactErrorComponent
                | ApiV1PrefixesListOrganizationsErrorComponent
                | ApiV1PrefixesListRegionErrorComponent
                | ApiV1PrefixesListSearchErrorComponent
                | ApiV1PrefixesListStateErrorComponent
                | ApiV1PrefixesListStateNotErrorComponent
                | ApiV1PrefixesListTimeRangeErrorComponent
                | ApiV1PrefixesListWorkspacesErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_list_error_type_0 = (
                        ApiV1PrefixesListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_list_error_type_1 = (
                        ApiV1PrefixesListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_list_error_type_2 = (
                        ApiV1PrefixesListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_list_error_type_3 = (
                        ApiV1PrefixesListWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_list_error_type_4 = (
                        ApiV1PrefixesListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_list_error_type_5 = ApiV1PrefixesListKindErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_prefixes_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_list_error_type_6 = (
                        ApiV1PrefixesListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_list_error_type_7 = (
                        ApiV1PrefixesListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_list_error_type_8 = (
                        ApiV1PrefixesListNameExactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_prefixes_list_error_type_9 = (
                        ApiV1PrefixesListLoadbalancerRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_prefixes_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_prefixes_list_error_type_10 = ApiV1PrefixesListRegionErrorComponent.from_dict(
                    data
                )

                return componentsschemas_api_v1_prefixes_list_error_type_10

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_prefixes_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_prefixes_list_validation_error.additional_properties = d
        return api_v1_prefixes_list_validation_error

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
