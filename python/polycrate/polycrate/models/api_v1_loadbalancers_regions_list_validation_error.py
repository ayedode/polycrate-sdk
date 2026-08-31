from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_loadbalancers_regions_list_created_at_error_component import (
        ApiV1LoadbalancersRegionsListCreatedAtErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_list_created_by_component_error_component import (
        ApiV1LoadbalancersRegionsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_list_created_by_users_error_component import (
        ApiV1LoadbalancersRegionsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_list_kind_error_component import (
        ApiV1LoadbalancersRegionsListKindErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_list_name_error_component import (
        ApiV1LoadbalancersRegionsListNameErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_list_name_exact_error_component import (
        ApiV1LoadbalancersRegionsListNameExactErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_list_organizations_error_component import (
        ApiV1LoadbalancersRegionsListOrganizationsErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_list_scope_error_component import (
        ApiV1LoadbalancersRegionsListScopeErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_list_search_error_component import (
        ApiV1LoadbalancersRegionsListSearchErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_list_state_error_component import (
        ApiV1LoadbalancersRegionsListStateErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_list_state_not_error_component import (
        ApiV1LoadbalancersRegionsListStateNotErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_list_time_range_error_component import (
        ApiV1LoadbalancersRegionsListTimeRangeErrorComponent,
    )
    from ..models.api_v1_loadbalancers_regions_list_updated_at_error_component import (
        ApiV1LoadbalancersRegionsListUpdatedAtErrorComponent,
    )


T = TypeVar("T", bound="ApiV1LoadbalancersRegionsListValidationError")


@_attrs_define
class ApiV1LoadbalancersRegionsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1LoadbalancersRegionsListCreatedAtErrorComponent |
            ApiV1LoadbalancersRegionsListCreatedByComponentErrorComponent |
            ApiV1LoadbalancersRegionsListCreatedByUsersErrorComponent | ApiV1LoadbalancersRegionsListKindErrorComponent |
            ApiV1LoadbalancersRegionsListNameErrorComponent | ApiV1LoadbalancersRegionsListNameExactErrorComponent |
            ApiV1LoadbalancersRegionsListOrganizationsErrorComponent | ApiV1LoadbalancersRegionsListScopeErrorComponent |
            ApiV1LoadbalancersRegionsListSearchErrorComponent | ApiV1LoadbalancersRegionsListStateErrorComponent |
            ApiV1LoadbalancersRegionsListStateNotErrorComponent | ApiV1LoadbalancersRegionsListTimeRangeErrorComponent |
            ApiV1LoadbalancersRegionsListUpdatedAtErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1LoadbalancersRegionsListCreatedAtErrorComponent
        | ApiV1LoadbalancersRegionsListCreatedByComponentErrorComponent
        | ApiV1LoadbalancersRegionsListCreatedByUsersErrorComponent
        | ApiV1LoadbalancersRegionsListKindErrorComponent
        | ApiV1LoadbalancersRegionsListNameErrorComponent
        | ApiV1LoadbalancersRegionsListNameExactErrorComponent
        | ApiV1LoadbalancersRegionsListOrganizationsErrorComponent
        | ApiV1LoadbalancersRegionsListScopeErrorComponent
        | ApiV1LoadbalancersRegionsListSearchErrorComponent
        | ApiV1LoadbalancersRegionsListStateErrorComponent
        | ApiV1LoadbalancersRegionsListStateNotErrorComponent
        | ApiV1LoadbalancersRegionsListTimeRangeErrorComponent
        | ApiV1LoadbalancersRegionsListUpdatedAtErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_loadbalancers_regions_list_created_at_error_component import (
            ApiV1LoadbalancersRegionsListCreatedAtErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_created_by_component_error_component import (
            ApiV1LoadbalancersRegionsListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_created_by_users_error_component import (
            ApiV1LoadbalancersRegionsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_kind_error_component import (
            ApiV1LoadbalancersRegionsListKindErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_name_error_component import (
            ApiV1LoadbalancersRegionsListNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_organizations_error_component import (
            ApiV1LoadbalancersRegionsListOrganizationsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_scope_error_component import (
            ApiV1LoadbalancersRegionsListScopeErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_search_error_component import (
            ApiV1LoadbalancersRegionsListSearchErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_state_error_component import (
            ApiV1LoadbalancersRegionsListStateErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_state_not_error_component import (
            ApiV1LoadbalancersRegionsListStateNotErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_time_range_error_component import (
            ApiV1LoadbalancersRegionsListTimeRangeErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_updated_at_error_component import (
            ApiV1LoadbalancersRegionsListUpdatedAtErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1LoadbalancersRegionsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1LoadbalancersRegionsListStateNotErrorComponent):
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
        from ..models.api_v1_loadbalancers_regions_list_created_at_error_component import (
            ApiV1LoadbalancersRegionsListCreatedAtErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_created_by_component_error_component import (
            ApiV1LoadbalancersRegionsListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_created_by_users_error_component import (
            ApiV1LoadbalancersRegionsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_kind_error_component import (
            ApiV1LoadbalancersRegionsListKindErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_name_error_component import (
            ApiV1LoadbalancersRegionsListNameErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_name_exact_error_component import (
            ApiV1LoadbalancersRegionsListNameExactErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_organizations_error_component import (
            ApiV1LoadbalancersRegionsListOrganizationsErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_scope_error_component import (
            ApiV1LoadbalancersRegionsListScopeErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_search_error_component import (
            ApiV1LoadbalancersRegionsListSearchErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_state_error_component import (
            ApiV1LoadbalancersRegionsListStateErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_state_not_error_component import (
            ApiV1LoadbalancersRegionsListStateNotErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_time_range_error_component import (
            ApiV1LoadbalancersRegionsListTimeRangeErrorComponent,
        )
        from ..models.api_v1_loadbalancers_regions_list_updated_at_error_component import (
            ApiV1LoadbalancersRegionsListUpdatedAtErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1LoadbalancersRegionsListCreatedAtErrorComponent
                | ApiV1LoadbalancersRegionsListCreatedByComponentErrorComponent
                | ApiV1LoadbalancersRegionsListCreatedByUsersErrorComponent
                | ApiV1LoadbalancersRegionsListKindErrorComponent
                | ApiV1LoadbalancersRegionsListNameErrorComponent
                | ApiV1LoadbalancersRegionsListNameExactErrorComponent
                | ApiV1LoadbalancersRegionsListOrganizationsErrorComponent
                | ApiV1LoadbalancersRegionsListScopeErrorComponent
                | ApiV1LoadbalancersRegionsListSearchErrorComponent
                | ApiV1LoadbalancersRegionsListStateErrorComponent
                | ApiV1LoadbalancersRegionsListStateNotErrorComponent
                | ApiV1LoadbalancersRegionsListTimeRangeErrorComponent
                | ApiV1LoadbalancersRegionsListUpdatedAtErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_list_error_type_0 = (
                        ApiV1LoadbalancersRegionsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_list_error_type_1 = (
                        ApiV1LoadbalancersRegionsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_list_error_type_2 = (
                        ApiV1LoadbalancersRegionsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_list_error_type_3 = (
                        ApiV1LoadbalancersRegionsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_list_error_type_4 = (
                        ApiV1LoadbalancersRegionsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_list_error_type_5 = (
                        ApiV1LoadbalancersRegionsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_list_error_type_6 = (
                        ApiV1LoadbalancersRegionsListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_list_error_type_7 = (
                        ApiV1LoadbalancersRegionsListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_list_error_type_8 = (
                        ApiV1LoadbalancersRegionsListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_list_error_type_9 = (
                        ApiV1LoadbalancersRegionsListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_list_error_type_10 = (
                        ApiV1LoadbalancersRegionsListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_loadbalancers_regions_list_error_type_11 = (
                        ApiV1LoadbalancersRegionsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_loadbalancers_regions_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_loadbalancers_regions_list_error_type_12 = (
                    ApiV1LoadbalancersRegionsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_loadbalancers_regions_list_error_type_12

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_loadbalancers_regions_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_loadbalancers_regions_list_validation_error.additional_properties = d
        return api_v1_loadbalancers_regions_list_validation_error

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
