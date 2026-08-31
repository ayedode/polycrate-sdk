from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_domains_list_created_at_error_component import (
        ApiV1DomainsDomainsListCreatedAtErrorComponent,
    )
    from ..models.api_v1_domains_domains_list_created_by_component_error_component import (
        ApiV1DomainsDomainsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_domains_list_created_by_users_error_component import (
        ApiV1DomainsDomainsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_domains_domains_list_dns_zone_error_component import (
        ApiV1DomainsDomainsListDnsZoneErrorComponent,
    )
    from ..models.api_v1_domains_domains_list_expiry_before_error_component import (
        ApiV1DomainsDomainsListExpiryBeforeErrorComponent,
    )
    from ..models.api_v1_domains_domains_list_kind_error_component import ApiV1DomainsDomainsListKindErrorComponent
    from ..models.api_v1_domains_domains_list_name_error_component import ApiV1DomainsDomainsListNameErrorComponent
    from ..models.api_v1_domains_domains_list_name_exact_error_component import (
        ApiV1DomainsDomainsListNameExactErrorComponent,
    )
    from ..models.api_v1_domains_domains_list_organizations_error_component import (
        ApiV1DomainsDomainsListOrganizationsErrorComponent,
    )
    from ..models.api_v1_domains_domains_list_registrar_error_component import (
        ApiV1DomainsDomainsListRegistrarErrorComponent,
    )
    from ..models.api_v1_domains_domains_list_scope_error_component import ApiV1DomainsDomainsListScopeErrorComponent
    from ..models.api_v1_domains_domains_list_search_error_component import ApiV1DomainsDomainsListSearchErrorComponent
    from ..models.api_v1_domains_domains_list_state_error_component import ApiV1DomainsDomainsListStateErrorComponent
    from ..models.api_v1_domains_domains_list_state_not_error_component import (
        ApiV1DomainsDomainsListStateNotErrorComponent,
    )
    from ..models.api_v1_domains_domains_list_time_range_error_component import (
        ApiV1DomainsDomainsListTimeRangeErrorComponent,
    )
    from ..models.api_v1_domains_domains_list_updated_at_error_component import (
        ApiV1DomainsDomainsListUpdatedAtErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDomainsListValidationError")


@_attrs_define
class ApiV1DomainsDomainsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDomainsListCreatedAtErrorComponent |
            ApiV1DomainsDomainsListCreatedByComponentErrorComponent | ApiV1DomainsDomainsListCreatedByUsersErrorComponent |
            ApiV1DomainsDomainsListDnsZoneErrorComponent | ApiV1DomainsDomainsListExpiryBeforeErrorComponent |
            ApiV1DomainsDomainsListKindErrorComponent | ApiV1DomainsDomainsListNameErrorComponent |
            ApiV1DomainsDomainsListNameExactErrorComponent | ApiV1DomainsDomainsListOrganizationsErrorComponent |
            ApiV1DomainsDomainsListRegistrarErrorComponent | ApiV1DomainsDomainsListScopeErrorComponent |
            ApiV1DomainsDomainsListSearchErrorComponent | ApiV1DomainsDomainsListStateErrorComponent |
            ApiV1DomainsDomainsListStateNotErrorComponent | ApiV1DomainsDomainsListTimeRangeErrorComponent |
            ApiV1DomainsDomainsListUpdatedAtErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDomainsListCreatedAtErrorComponent
        | ApiV1DomainsDomainsListCreatedByComponentErrorComponent
        | ApiV1DomainsDomainsListCreatedByUsersErrorComponent
        | ApiV1DomainsDomainsListDnsZoneErrorComponent
        | ApiV1DomainsDomainsListExpiryBeforeErrorComponent
        | ApiV1DomainsDomainsListKindErrorComponent
        | ApiV1DomainsDomainsListNameErrorComponent
        | ApiV1DomainsDomainsListNameExactErrorComponent
        | ApiV1DomainsDomainsListOrganizationsErrorComponent
        | ApiV1DomainsDomainsListRegistrarErrorComponent
        | ApiV1DomainsDomainsListScopeErrorComponent
        | ApiV1DomainsDomainsListSearchErrorComponent
        | ApiV1DomainsDomainsListStateErrorComponent
        | ApiV1DomainsDomainsListStateNotErrorComponent
        | ApiV1DomainsDomainsListTimeRangeErrorComponent
        | ApiV1DomainsDomainsListUpdatedAtErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_domains_list_created_at_error_component import (
            ApiV1DomainsDomainsListCreatedAtErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_created_by_component_error_component import (
            ApiV1DomainsDomainsListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_created_by_users_error_component import (
            ApiV1DomainsDomainsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_dns_zone_error_component import (
            ApiV1DomainsDomainsListDnsZoneErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_expiry_before_error_component import (
            ApiV1DomainsDomainsListExpiryBeforeErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_kind_error_component import ApiV1DomainsDomainsListKindErrorComponent
        from ..models.api_v1_domains_domains_list_name_error_component import ApiV1DomainsDomainsListNameErrorComponent
        from ..models.api_v1_domains_domains_list_organizations_error_component import (
            ApiV1DomainsDomainsListOrganizationsErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_registrar_error_component import (
            ApiV1DomainsDomainsListRegistrarErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_scope_error_component import (
            ApiV1DomainsDomainsListScopeErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_search_error_component import (
            ApiV1DomainsDomainsListSearchErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_state_error_component import (
            ApiV1DomainsDomainsListStateErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_state_not_error_component import (
            ApiV1DomainsDomainsListStateNotErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_time_range_error_component import (
            ApiV1DomainsDomainsListTimeRangeErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_updated_at_error_component import (
            ApiV1DomainsDomainsListUpdatedAtErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDomainsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsListOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsListDnsZoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsListRegistrarErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsListExpiryBeforeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsListStateNotErrorComponent):
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
        from ..models.api_v1_domains_domains_list_created_at_error_component import (
            ApiV1DomainsDomainsListCreatedAtErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_created_by_component_error_component import (
            ApiV1DomainsDomainsListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_created_by_users_error_component import (
            ApiV1DomainsDomainsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_dns_zone_error_component import (
            ApiV1DomainsDomainsListDnsZoneErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_expiry_before_error_component import (
            ApiV1DomainsDomainsListExpiryBeforeErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_kind_error_component import ApiV1DomainsDomainsListKindErrorComponent
        from ..models.api_v1_domains_domains_list_name_error_component import ApiV1DomainsDomainsListNameErrorComponent
        from ..models.api_v1_domains_domains_list_name_exact_error_component import (
            ApiV1DomainsDomainsListNameExactErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_organizations_error_component import (
            ApiV1DomainsDomainsListOrganizationsErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_registrar_error_component import (
            ApiV1DomainsDomainsListRegistrarErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_scope_error_component import (
            ApiV1DomainsDomainsListScopeErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_search_error_component import (
            ApiV1DomainsDomainsListSearchErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_state_error_component import (
            ApiV1DomainsDomainsListStateErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_state_not_error_component import (
            ApiV1DomainsDomainsListStateNotErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_time_range_error_component import (
            ApiV1DomainsDomainsListTimeRangeErrorComponent,
        )
        from ..models.api_v1_domains_domains_list_updated_at_error_component import (
            ApiV1DomainsDomainsListUpdatedAtErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDomainsListCreatedAtErrorComponent
                | ApiV1DomainsDomainsListCreatedByComponentErrorComponent
                | ApiV1DomainsDomainsListCreatedByUsersErrorComponent
                | ApiV1DomainsDomainsListDnsZoneErrorComponent
                | ApiV1DomainsDomainsListExpiryBeforeErrorComponent
                | ApiV1DomainsDomainsListKindErrorComponent
                | ApiV1DomainsDomainsListNameErrorComponent
                | ApiV1DomainsDomainsListNameExactErrorComponent
                | ApiV1DomainsDomainsListOrganizationsErrorComponent
                | ApiV1DomainsDomainsListRegistrarErrorComponent
                | ApiV1DomainsDomainsListScopeErrorComponent
                | ApiV1DomainsDomainsListSearchErrorComponent
                | ApiV1DomainsDomainsListStateErrorComponent
                | ApiV1DomainsDomainsListStateNotErrorComponent
                | ApiV1DomainsDomainsListTimeRangeErrorComponent
                | ApiV1DomainsDomainsListUpdatedAtErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_list_error_type_0 = (
                        ApiV1DomainsDomainsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_list_error_type_1 = (
                        ApiV1DomainsDomainsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_list_error_type_2 = (
                        ApiV1DomainsDomainsListOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_list_error_type_3 = (
                        ApiV1DomainsDomainsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_list_error_type_4 = (
                        ApiV1DomainsDomainsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_list_error_type_5 = (
                        ApiV1DomainsDomainsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_list_error_type_6 = (
                        ApiV1DomainsDomainsListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_list_error_type_7 = (
                        ApiV1DomainsDomainsListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_list_error_type_8 = (
                        ApiV1DomainsDomainsListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_list_error_type_9 = (
                        ApiV1DomainsDomainsListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_list_error_type_10 = (
                        ApiV1DomainsDomainsListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_list_error_type_11 = (
                        ApiV1DomainsDomainsListDnsZoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_list_error_type_12 = (
                        ApiV1DomainsDomainsListRegistrarErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_list_error_type_13 = (
                        ApiV1DomainsDomainsListExpiryBeforeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_list_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_list_error_type_14 = (
                        ApiV1DomainsDomainsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_list_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_domains_list_error_type_15 = (
                    ApiV1DomainsDomainsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_domains_list_error_type_15

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_domains_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_domains_list_validation_error.additional_properties = d
        return api_v1_domains_domains_list_validation_error

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
