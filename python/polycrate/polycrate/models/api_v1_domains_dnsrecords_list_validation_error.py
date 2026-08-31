from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_dnsrecords_list_created_at_error_component import (
        ApiV1DomainsDnsrecordsListCreatedAtErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_list_created_by_component_error_component import (
        ApiV1DomainsDnsrecordsListCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_list_created_by_users_error_component import (
        ApiV1DomainsDnsrecordsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_list_dns_zone_error_component import (
        ApiV1DomainsDnsrecordsListDnsZoneErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_list_kind_error_component import (
        ApiV1DomainsDnsrecordsListKindErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_list_name_error_component import (
        ApiV1DomainsDnsrecordsListNameErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_list_name_exact_error_component import (
        ApiV1DomainsDnsrecordsListNameExactErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_list_scope_error_component import (
        ApiV1DomainsDnsrecordsListScopeErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_list_search_error_component import (
        ApiV1DomainsDnsrecordsListSearchErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_list_state_error_component import (
        ApiV1DomainsDnsrecordsListStateErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_list_state_not_error_component import (
        ApiV1DomainsDnsrecordsListStateNotErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_list_time_range_error_component import (
        ApiV1DomainsDnsrecordsListTimeRangeErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_list_type_error_component import (
        ApiV1DomainsDnsrecordsListTypeErrorComponent,
    )
    from ..models.api_v1_domains_dnsrecords_list_updated_at_error_component import (
        ApiV1DomainsDnsrecordsListUpdatedAtErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDnsrecordsListValidationError")


@_attrs_define
class ApiV1DomainsDnsrecordsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDnsrecordsListCreatedAtErrorComponent |
            ApiV1DomainsDnsrecordsListCreatedByComponentErrorComponent |
            ApiV1DomainsDnsrecordsListCreatedByUsersErrorComponent | ApiV1DomainsDnsrecordsListDnsZoneErrorComponent |
            ApiV1DomainsDnsrecordsListKindErrorComponent | ApiV1DomainsDnsrecordsListNameErrorComponent |
            ApiV1DomainsDnsrecordsListNameExactErrorComponent | ApiV1DomainsDnsrecordsListScopeErrorComponent |
            ApiV1DomainsDnsrecordsListSearchErrorComponent | ApiV1DomainsDnsrecordsListStateErrorComponent |
            ApiV1DomainsDnsrecordsListStateNotErrorComponent | ApiV1DomainsDnsrecordsListTimeRangeErrorComponent |
            ApiV1DomainsDnsrecordsListTypeErrorComponent | ApiV1DomainsDnsrecordsListUpdatedAtErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDnsrecordsListCreatedAtErrorComponent
        | ApiV1DomainsDnsrecordsListCreatedByComponentErrorComponent
        | ApiV1DomainsDnsrecordsListCreatedByUsersErrorComponent
        | ApiV1DomainsDnsrecordsListDnsZoneErrorComponent
        | ApiV1DomainsDnsrecordsListKindErrorComponent
        | ApiV1DomainsDnsrecordsListNameErrorComponent
        | ApiV1DomainsDnsrecordsListNameExactErrorComponent
        | ApiV1DomainsDnsrecordsListScopeErrorComponent
        | ApiV1DomainsDnsrecordsListSearchErrorComponent
        | ApiV1DomainsDnsrecordsListStateErrorComponent
        | ApiV1DomainsDnsrecordsListStateNotErrorComponent
        | ApiV1DomainsDnsrecordsListTimeRangeErrorComponent
        | ApiV1DomainsDnsrecordsListTypeErrorComponent
        | ApiV1DomainsDnsrecordsListUpdatedAtErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_dnsrecords_list_created_at_error_component import (
            ApiV1DomainsDnsrecordsListCreatedAtErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_created_by_component_error_component import (
            ApiV1DomainsDnsrecordsListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_created_by_users_error_component import (
            ApiV1DomainsDnsrecordsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_dns_zone_error_component import (
            ApiV1DomainsDnsrecordsListDnsZoneErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_kind_error_component import (
            ApiV1DomainsDnsrecordsListKindErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_name_error_component import (
            ApiV1DomainsDnsrecordsListNameErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_scope_error_component import (
            ApiV1DomainsDnsrecordsListScopeErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_search_error_component import (
            ApiV1DomainsDnsrecordsListSearchErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_state_error_component import (
            ApiV1DomainsDnsrecordsListStateErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_state_not_error_component import (
            ApiV1DomainsDnsrecordsListStateNotErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_time_range_error_component import (
            ApiV1DomainsDnsrecordsListTimeRangeErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_type_error_component import (
            ApiV1DomainsDnsrecordsListTypeErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_updated_at_error_component import (
            ApiV1DomainsDnsrecordsListUpdatedAtErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDnsrecordsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsListCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsListNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsListCreatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsListUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsListScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsListDnsZoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsListTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnsrecordsListStateNotErrorComponent):
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
        from ..models.api_v1_domains_dnsrecords_list_created_at_error_component import (
            ApiV1DomainsDnsrecordsListCreatedAtErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_created_by_component_error_component import (
            ApiV1DomainsDnsrecordsListCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_created_by_users_error_component import (
            ApiV1DomainsDnsrecordsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_dns_zone_error_component import (
            ApiV1DomainsDnsrecordsListDnsZoneErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_kind_error_component import (
            ApiV1DomainsDnsrecordsListKindErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_name_error_component import (
            ApiV1DomainsDnsrecordsListNameErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_name_exact_error_component import (
            ApiV1DomainsDnsrecordsListNameExactErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_scope_error_component import (
            ApiV1DomainsDnsrecordsListScopeErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_search_error_component import (
            ApiV1DomainsDnsrecordsListSearchErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_state_error_component import (
            ApiV1DomainsDnsrecordsListStateErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_state_not_error_component import (
            ApiV1DomainsDnsrecordsListStateNotErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_time_range_error_component import (
            ApiV1DomainsDnsrecordsListTimeRangeErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_type_error_component import (
            ApiV1DomainsDnsrecordsListTypeErrorComponent,
        )
        from ..models.api_v1_domains_dnsrecords_list_updated_at_error_component import (
            ApiV1DomainsDnsrecordsListUpdatedAtErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDnsrecordsListCreatedAtErrorComponent
                | ApiV1DomainsDnsrecordsListCreatedByComponentErrorComponent
                | ApiV1DomainsDnsrecordsListCreatedByUsersErrorComponent
                | ApiV1DomainsDnsrecordsListDnsZoneErrorComponent
                | ApiV1DomainsDnsrecordsListKindErrorComponent
                | ApiV1DomainsDnsrecordsListNameErrorComponent
                | ApiV1DomainsDnsrecordsListNameExactErrorComponent
                | ApiV1DomainsDnsrecordsListScopeErrorComponent
                | ApiV1DomainsDnsrecordsListSearchErrorComponent
                | ApiV1DomainsDnsrecordsListStateErrorComponent
                | ApiV1DomainsDnsrecordsListStateNotErrorComponent
                | ApiV1DomainsDnsrecordsListTimeRangeErrorComponent
                | ApiV1DomainsDnsrecordsListTypeErrorComponent
                | ApiV1DomainsDnsrecordsListUpdatedAtErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_list_error_type_0 = (
                        ApiV1DomainsDnsrecordsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_list_error_type_1 = (
                        ApiV1DomainsDnsrecordsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_list_error_type_2 = (
                        ApiV1DomainsDnsrecordsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_list_error_type_3 = (
                        ApiV1DomainsDnsrecordsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_list_error_type_4 = (
                        ApiV1DomainsDnsrecordsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_list_error_type_5 = (
                        ApiV1DomainsDnsrecordsListCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_list_error_type_6 = (
                        ApiV1DomainsDnsrecordsListNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_list_error_type_7 = (
                        ApiV1DomainsDnsrecordsListCreatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_list_error_type_8 = (
                        ApiV1DomainsDnsrecordsListUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_list_error_type_9 = (
                        ApiV1DomainsDnsrecordsListScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_list_error_type_10 = (
                        ApiV1DomainsDnsrecordsListDnsZoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_list_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_list_error_type_11 = (
                        ApiV1DomainsDnsrecordsListTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_list_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnsrecords_list_error_type_12 = (
                        ApiV1DomainsDnsrecordsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnsrecords_list_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_dnsrecords_list_error_type_13 = (
                    ApiV1DomainsDnsrecordsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_dnsrecords_list_error_type_13

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_dnsrecords_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_dnsrecords_list_validation_error.additional_properties = d
        return api_v1_domains_dnsrecords_list_validation_error

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
